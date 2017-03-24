"""
Provide the FBSMunger class for munging the Food Balance Sheet.
"""
import os
import csv

from effayoh.util import FAOSTAT_DIR
from effayoh.mungers import FAOCountry


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

    def __new__(cls, items):
        return super().__new__(cls, items)


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

    def __new__(cls, elements):
        return super().__new__(cls, elements)


class FBSItemsElementsGroup(tuple):

    __slots__ = ["attr_name"]
    object_pool = {}

    def __new__(cls, attr_name, items_group, elements_group):
        if not isinstance(items_group, FBSItemGroup):
            raise TypeError("items_group must be an FBSItemGroup")
        if not isinstance(elements_group, FBSElementGroup):
            raise TypeError("elements_group must be an FBSElementGroup")
        tup = (items_group, elements_group)
        if tup in FBSItemsElementsGroup.object_pool:
            return FBSItemsElementsGroup.object_pool[tup]
        else:
            obj = super().__new__(cls, tup)
            FBSItemsElementsGroup.object_pool[obj] = obj
            return obj

    def __init__(self, attr_name, items_group, elements_group):
        self.attr_name = attr_name


class FBSMunger:
    """
    Data munger for the FAO Food Balance Sheet data.

    """

    # We want to extract production and consumption.
    # Production consists in one element and a group of items.
    # Consumption consits in a group of elements and a group
    # of items.

    def __init__(self, political_rectifier):
        self.years = None
        self.items = set()
        self.elements = set()
        self.item_element_conversions = {}
        self.items_elements_groups = set()
        self.items_elements_groups_conversions = {}
        self.political_rectifier = political_rectifier

    def set_years(self, years):
        self.years = years

    def add_item(self, item):
        self.items.add(item)

    def add_items(self, items):
        for item in items:
            self.add_item(item)

    def set_item_element_conversion(self, item, element, conversion):
        if not isinstance(item, FBSItem):
            raise TypeError("item must be a FBSItem")
        if not isinstance(element, FBSElement):
            raise TypeError("element must be an FBSElement")
        if not callable(conversion):
            raise TypeError("conversion must be callable")
        key = (item, element)
        self.item_element_conversions[key] = conversion

    def add_element(self, element):
        self.elements.add(element)

    def add_elements(self, elements):
        for element in elements:
            self.add_element(element)

    def add_items_elements_group(self, items_group, elements_group):
        self.add_items(self, items_group)
        self.add_elements(self, elements_group)
        self.items_elements_groups.add((items_group, elements_group))

    def set_items_elements_group_conversion(self,
                                            items_group,
                                            elements_group,
                                            conversion):
        if not isinstance(items_group, FBSItemGroup):
            raise TypeError("items_group must be an FBSItemGroup")
        if not isinstance(elements_group, FBSElementGroup):
            raise TypeError("elements_group must be an FBSElementGroup")
        if not callable(conversion):
            raise TypeError("conversion must be a callable")
        key = (items_group, elements_group)
        self.items_elements_groups_conversions[key] = conversion

    def munge(self):
        """
        Extract and process data in FAO Food Balance Sheet.
        """
        data = self.get_raw_data()

        # Apply the item-element conversions.
        for country, items in data.items():
            for item, elements in items.items():
                for element, years in elements.items():
                    mean = sum(years.values()) / len(self.years)
                    func = self.item_element_conversions.get(
                        key,
                        lambda x: x
                    )
                    value = func(mean)
                    elements[element] = value

        # Apply items-elements groups conversions.
        for group in self.items_elements_groups:
            items, elements = group
            for country, citems in data.items():
                for item, elements in citems.items():
                    if not item in items:
                        continue

                    func = self.items_elements_groups_conversions.get(
                        group,
                        lambda x: sum(x.values())
                    )

                    args = {(item, element): elements[element]
                            for element in elements}

                    value = func(args)
                    self.set_network_node_attr(country,
                                               group.attr_name
                                               value)

    def get_raw_data(self):
        """
        Return a dict of country data for the selected items and years.

        The dict is four dimensional keying on Country, Item, Element
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

                country = FAOCountry(
                    row["Area"],
                    row["Area Code"]
                )

                item_dict = data.setdefault(country, {})
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
