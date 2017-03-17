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


class FBSElement(tuple):

    __slots__ = []
    object_pool = {}

    def __new__(cls, element, code):
        tup = (element, code)
        if tup in FBSElement.object_pool:
            return FBSElement.object_pool[tup]
        else:
            obj = super().__new__(cls, tup)
            FBSElement.object_pool[obj] = obj
            return obj


class FBSElementGroup(frozenset):

    __slots__ = ["attr_name"]

    def __new__(cls, elements, attr_name):
        return super().__new__(cls, elements)

    def __init__(self, elements, attr_name):
        self.attr_name = attr_name


class FBSMunger:
    """
    Data munger for the FAO Food Balance Sheet data.

    """

    def __init__(self, political_rectifier):
        self.years = None
        self.items = set()
        self.elements = set()
        self.element_attrs = set()
        self.element_groups = set()
        self.element_conversions = {}
        self.element_group_conversions = {}
        self.political_rectifier = political_rectifier

    def set_years(self, years):
        self.years = years

    def add_item(self, item):
        self.items.add(item)

    def add_items(self, items):
        for item in items:
            self.add_item(item)

    def add_element(self, element, mk_attr=False):
        self.elements.add(element)
        if mk_attr:
            self.element_attrs.add(element)

    def add_elements(self, elements):
        for element in elements:
            self.add_element(element)

    def add_element_group(self, group):
        self.element_groups.add(group)
        self.add_elements(group)

    def add_element_groups(self, groups):
        for group in groups:
            self.add_element_group(group)

    def set_element_conversion(self, element, conversion):
        if not isinstance(element, FBSElement):
            raise TypeError("element must be an FBSElement")
        if not callable(conversion):
            raise TypeError("conversion must be a callable.")
        self.element_conversions[element] = conversion

    def set_element_group_conversion(self, group, conversion):
        if not isinstance(group, FBSElementGroup):
            raise TypeError("group must be an FBSElementGroup")
        if not callable(conversion):
            raise TypeError("conversion must be a callable.")
        self.element_group_conversions[group] = conversion

    def munge(self):
        """
        Extract and process data in FAO Food Balance Sheet.
        """
        data = self.get_raw_data()

        # Apply the element-wise conversions.
        for political_entity, items in data.items():
            for item, elements in items.items():
                for element, years in elements.items():
                    mean = sum(years.values()) / len(self.years)
                    func = self.element_conversions.get(item, lambda x: x)
                    value = func(mean)
                    elements[element] = value

                    if element in self.element_attrs:
                        name, _ = item
                        self.set_network_node_attr(political_entity,
                                                   name,
                                                   value)

        # Apply the group-wise conversions.
        for group in self.element_groups:
            for political_entity, items in data.items():
                for item, elements in items.items():
                    func = self.element_group_conversions.get(
                        group,
                        lambda x: sum(x.values())
                    )
                    value = func({element: elements[element]
                                  for element in elements
                                  if element in group})
                    self.set_network_node_attr(political_entity,
                                               group.attr_name,
                                               value)

    def get_raw_data(self):
        """
        Return a dict of country data for the selected items and years.

        The dict is four dimensional keying on Area Code, Item, Element
        and Year.
        """
        data_path = os.path.join(FAOSTAT_DIR,
                                 "food-balance-sheets",
                                 "FoodBalanceSheets_E_All_Data.csv")

        data = {}
        years_fields = [(year, "Y" + str(year)) for year in years]

        with open(data_path, encoding="latin1") as csv_file:

            reader = csv.DictReader(csv_file)

            for row in reader:

                item = FBSItem(row["Item"], row["Item Code"])
                if not item in self.items:
                    continue

                element = FBSElement(row["Element"], row["Element Code"])
                if not element in self.elements:
                    continue

                # The row has one of the target item codes and one of
                # the target element codes but it might not have a value
                # for any of the years. We do the check here to avoid
                # creating chains of dicts in the data that ultimately
                # have no values.
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
                elem_dict = item_dict.setdefault(item, {})
                year_dict = elem_dict.setdefault(element, {})

                for year, value in year_values:
                    year_dict[year] = value

        self.data = data

        return data

    def set_network_node_attr(self, country, name, value):
        self.political_rectifier.set_network_node_attr(
            country,
            name,
            value
        )
