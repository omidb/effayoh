import os
import csv

EFFAYOH_DIR, _ = os.path.split(__file__)
RESOURCES_DIR = os.path.join(EFFAYOH_DIR, "resources")
FAOSTAT_DIR = os.path.join(RESOURCES_DIR, "faostat")

def get_FAO_country_codes():
    """ Return a list of the FAO country codes. """
    code_path = os.path.join(FAOSTAT_DIR,
                             "definitions-and-standards",
                             "country-region-3-8-2017.csv")

    with open(code_path) as csv_file:
        reader = csv.DictReader(csv_file)
        codes = [row["Country Code"] for row in reader]

    return codes

def get_food_balance_sheet_data(items, years):
    """
    Return a dict of country data for the selected items and years.

    The dict is keyed on FAO country code. Each country code is in turn
    mapped to another dict keyed on item code. Each item code is in turn
    mapped to another dict keyed on year. The years are mapped to the
    value published in the FAO data for that country/item row. Said
    another way:

    Country Code Dict -> Item Code Dict -> Year Dict -> value

    {
        "Item Code": {
            "Country Code": {
                "Year": 1097,
                ...
            }
            ...
        }
        ...
    }

    So for example assuming "2501" is one of the items and "2013" is one
    of the years then data["2"]["2501"]["2013"] yields 30552.000000
    which indicates a total population of 30.552 million people in
    Afghanistan in 2013.

    """
    data_path = os.path.join(FAOSTAT_DIR,
                             "food-balance-sheets",
                             "FoodBalanceSheets_E_All_Data.csv")

    data = {}


    years_fields = [(year, "Y" + str(year)) for year in years]

    with open(data_path, encoding="latin1") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            item_code = row["Item Code"]
            if not item_code in items:
                continue
            country = row["Area Code"]
            item_dict = data.setdefault(country, {})
            year_dict = item_dict.setdefault(item_code, {})
            for year, field in years_fields:
                year_dict[year] = row[field]

    return data

def get_detailed_trade_matrix_data(items, elements, years):
    """
    Return a dict of country data for the selected items and years.

    Returns:
        A dict with hierarchical structure. The first level of the dict
        maps Reporter Country Codes. The second level maps to Partner
        Country Codes. The third level maps to Element Codes. The fourth
        level maps to Item Code. The fifth level maps Years to values.
        As in:

        Reporter Country Code
            Partner Country Code
                Element Code
                    Item Code
                        Year
                            Value

        For example:

        Afghanistan
            Iran
                Exports
                    Wheat
                        2013
                            1025

    """
    data_path = os.path.join(FAOSTAT_DIR,
                             "detailed-trade-matrix",
                             "Trade_DetailedTradeMatrix_E_All_Data.csv")

    data = {}

    years_fields = [(year, "Y" + str(year)) for year in years]

    with open(data_path, encoding="latin1") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:

            item_code = row["Item Code"]
            if not item_code in items:
                continue

            element_code = row["Element Code"]
            if not element_code in elements:
                continue

            year_values = []
            for year, field in years_fields:
                try:
                    value = float(row[field])
                    year_values.append((year, value))
                except ValueError as ve:
                    pass

            if not year_values:
                continue

            reporter_country = row["Reporter Country Code"]
            partner_dict = data.setdefault(reporter_country, {})

            partner_country = row["Partner Country Code"]
            element_dict = partner_dict.setdefault(partner_country, {})

            item_dict = element_dict.setdefault(element_code, {})
            year_dict = item_dict.setdefault(item_code, {})

            for year, value in year_values:
                year_dict[year] = value

    return data
