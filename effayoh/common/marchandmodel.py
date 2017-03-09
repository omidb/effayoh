"""
:class MarchandModel:
    Implements the model of Marchand et al.

:class MarchandModelItem:
    Used by the MarchandModel as the basis of the trade network.
"""

from effayoh import util
from effayoh.network import Network


# PEP 8 guidance on class docstrings:
# The docstring for a class should summarize its behavior and list the public
# methods and instance variables.


class MarchandModelError(Exception): pass

class MarchandModel:

    """
    A model of global trade shock dynamics.

    The Marchand model is a model of the behavior of the global food
    trade network when a production shock occurs in one country.
    Rules are applied to propagate the shock and distribute the loss in
    production throughout the trade network.

    """

    def __init__(self):
        self.network = Network()
        self.static_params = None
        self.dynamic_params = None
        self.iteration_policy = None

class MarchandModelCommodity:
    pass

class MarchandModelBuilder:


    def __init__(self):
        self.aggregate_countries = {}
        self.network_initializers = []
        self.static_params = {}
        self.dynamic_params = {}
        self.iteration_policy = None
        self.years = []


    def add_network_initializer(self, initializer):
        """
        Add initializer to the collection of initializers.

        Inititializers will be executed in the order in which they are
        added to the builder. If an initializer, f, depends on a
        previous initializer, g, then it is up to the client code to
        add g to the builder before adding f.

        """
        if not callable(initializer):
            msg = "initializer must be a function."
            raise MarchandModelError(msg)

        signature = inspect.signature(initializer)
        if len(signature.parameters) != 1:
            msg = "initializer must be a monadic function."
            raise MarchandModelError(msg)

        self.network_initializers.append(initializer)


    def add_static_param(self, name, val):
        """ Add a static parameter to the builder. """
        self.static_params[name] = val


    def add_dynamic_param(self, name, func):
        """ Add a dynamic parameter to the builder. """
        if not callable(func):
            msg = "func must be a function."
            raise MarchandModelError(msg)

        self.dynamic_params[name] = func


    def set_iteration_policy(self, policy):
        """ Set the iteration policy for the model. """
        if not callable(policy):
            msg = "policy must be a function."
            raise MarchandModelError(msg)

        self.policy = policy


    def build(self, base=True):
        """ Return a built Marchand model. """
        model = MarchandModel()

        if base:
            self.setup_base_model()

        self.country_initializer(model.network)

        # Execute initializers.
        for initializer in self.network_initializers:
            initializer(model.network)

        # Add static parameters and dynamic parameters.
        model.static_params = self.static_params
        model.dynamic_params = self.dynamic_params

        # Set the update policy.
        model.iteration_policy = self.iteration_policy

        return model


    def country_initializer(self, network):
        """ Creates the nodes for the countries in network. """
        seen = set()

        for name, country_codes in self.aggregate_countries.items():
            # Update the aggregated_codes dict of network which maps
            # constituent country codes to their aggregates.
            codes2name = {code: name for code in country_codes}
            network.aggregated_codes.update(codes2name)

            code_nodes = {code: {} for code in country_codes}
            network.add_node(name, **code_nodes)
            seen |= set(country_codes)
            network

        FAO_country_codes = util.get_FAO_country_codes()

        for country_code in FAO_country_codes:
            if country_code in seen:
                continue
            network.add_node(country_code)
            seen.add(country_code)


    def setup_base_model(self):
        """ Set up the base model. """
        self.network_initializers[:0] = [self.base_initializer]
        self.iteration_policy = MarchandModelBuilder.base_iteration_policy

    def aggregate_country_codes(self, name, country_codes):
        """ Add aggregate country to the builder. """
        self.aggregate_countries[name] = country_codes

    def base_initializer(self, network):
        """
        The base initializer needs to know which items to grab in the
        food balance sheet, which items to grab from the detailed trade
        matrix sheet, which years to grab, and how to combine the items.
        """
        # Get the data from the UN FAOSTAT data sheets needed to
        # initialize the network.
        fbs_items = self.food_balance_sheet_items
        fbs_data = util.get_food_balance_sheet_data(fbs_items, self.years)

        dtm_items = self.detailed_trade_matrix_items
        dtm_data = util.get_detailed_trade_matrix_data(dtm_items, self.years)


    def set_years(self, years):
        """ Set the years to use. """
        self.years = years

    def set_food_balance_sheet_items(self, items):
        self.food_balance_sheet_items = items

    def set_detailed_trade_matrix(self, items):
        self.detailed_trade_matrix_items = items

    def set_default_item(self, item):
        if item.lower() == "wheat":
            self.set_food_balance_sheet_items(["2511"])
            self.set_detailed_trade_matrix([
                "15", "16", "17", "18", "19",
                "20", "21", "22", "23", "24",
                "41", "110", "114", "115"
            ])
        else:
            msg = "No item {item}".format(item=item)
            raise MarchandModelError(msg)

    @staticmethod
    def base_iteration_policy(model):
        pass
