"""
Provide the FBSMunger class for munging the Food Balance Sheet.
"""
import os
import csv

from util import FAOSTAT_DIR


class FBSItem(tuple):

    __slots__ = []
    object_pool = {}

    def __new__(cls, item, code):
        tup = (item, code)
        if tup in FBSItem.object_pool:
            return FBSItem.object_pool[tup]
        else:
            obj = super().__new__(cls, tup)
            FBSItem.object_pool[obj] = obj
            return obj


class FBSItemGroup(frozenset):

    __slots__ = ["attr_name"]

    def __new__(cls, items, attr_name):
        return super().__new__(cls, items)

    def __init__(self, items, attr_name):
        self.attr_name = attr_name


class FBSMunger:
    """
    Data munger for the FAO Food Balance Sheet data.

    """

    def __init__(self, political_rectifier):
        self.years = None
        self.items = set()
        self.item_attrs = set()
        self.groups = set()
        self.item_conversions = {}
        self.group_conversions = {}
        self.political_rectifier = political_rectifier

    def set_years(self, years):
        self.years = years

    def add_item(self, item, mk_attr=False):
        self.items.add(item)
        if mk_attr:
            self.item_attrs.add(item)

    def add_items(self, items):
        for item in items:
            self.add_item(item)

    def add_item_group(self, group):
        self.groups.add(group)
        self.add_items(group)

    def add_item_groups(self, groups):
        for group in groups:
            self.add_item_group(group)

    def set_item_conversion(self, item, conversion):
        if not isinstance(item, FBSItem):
            raise TypeError("item must be an FBSItem.")
        if not callable(conversion):
            raise TypeError("conversion must be a function.")
        self.item_conversions[item] = conversion

    def set_group_conversion(self, group, conversion):
        if not isinstance(group, FBSItemGroup):
            raise TypeError("group must be an FBSItemGroup.")
        if not callable(conversion):
            raise TypeError("conversion must be a function.")
        self.group_conversions[group] = conversion

    def munge(self):
        """
        Extract and process data in FAO Food Balance Sheet.
        """
        data = self.get_raw_data()

        # Apply the item-wise conversions.
        for political_entity, items in data.items():
            for item, years in items.items():
                mean = sum(years.values()) / len(self.years)
                func = self.item_conversions.get(item, lambda x: x)
                value = func(mean)
                items[item] = value

                if item in self.item_attrs:
                    name, _ = item
                    self.set_network_attr(political_entity, name, value)

        # Apply the group-wise conversions.
        for group in self.groups:
            for political_entity, items in data.items():
                func = self.group_conversions.get(
                    group,
                    lambda x: sum(x.values())
                )
                value = func({item: items[item] for item in items
                                                if item in group})
                self.set_network_attr(political_entity,
                                      group.attr_name,
                                      value)

    def get_raw_data(self):
        """
        Return a dict of country data for the selected items and years.
        """
        data_path = os.path.join(FAOSTAT_DIR,
                                 "food-balance-sheets",
                                 "FoodBalanceSheets_E_All_Data.csv")

        data = {}
        years_fields = [(year, "Y" + str(year)) for year in years]

        with open(data_path, encoding="latin1") as csv_file:

            reader = csv.DictReader(csv_file)

            for row in reader:

                item, code = row["Item"], row["Item Code"]
                if not (item, code) in self.items:
                    continue

                # The row has one of the target item codes but it might
                # not have a value for any of the years. We do the
                # check here to avoid creating chains of dicts in the
                # data that ultimately have no values.
                years_values = []
                for year, field in years_fields:
                    try:
                        value = float(row[field])
                        years_values.append((year, value))
                    except ValueError as ve:
                        pass

                if not year_values:
                    continue

                political_entity = row["Area Code"]
                item_dict = data.setdefault(political_entity, {})
                year_dict = item_dict.setdefault((item, code), {})

                for year, value in year_values:
                    year_dict[year] = value

        self.data = data

        return data

    def set_network_attr(self, political_entity, name, value):
        node = self.get_node(political_entity)
        node[name] = value

    def get_node(self, political_entity):
        return self.political_rectifier.get_node(political_entity)
