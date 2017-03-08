"""
:class MarchandModel:
    Implements the model of Marchand et al.

:class MarchandModelItem:
    Used by the MarchandModel as the basis of the trade network.
"""

from effayoh import util


# PEP 8 guidance on class docstrings:
# The docstring for a class should summarize its behavior and list the public
# methods and instance variables.


class MarchandModelError(Exception): pass


class MarchandModel:

    """
    A model of global trade shock dynamics.

    The Marchand model is a model of the behavior of the global food
    trade network when a production shock occurs in one country.
    Simplistic rules are applied to propagate the shock and distribute
    the loss in production throughout the trade network.

    The MarchandModel class implements the Marchand model and provides
    methods and initialization parameters for selecting different
    commodities, absorption and redistribution strategies, and
    executing the model with the shock applied to different countries
    and with varying magnitudes.


    Public methods:

        __getitem__:
            Specify the model time period.

        process_data:
            Process the data to extract information for the
            given commodity and time period.

        shock:
            Apply a shock to the model.

        render:
            Render the model to an image.

        list_food_balance_sheet_items:
            List the items defined in the food balance sheets
            definitions and standards. These are available
            commodities right out of the box.

    Public attributes:

        commodity:
            The commodity of the underlying network.


    """

    def __init__(self, commodity, years=None):
        if isinstance(commodity, MarchandModelCommodity):
            self.commodity = commodity
        else:
            self.commodity = MarchandModelCommodity(commodity)

        if years is not None:
            self.years = {year for year in years}

        self._processed_data = False

    def __getitem__(self, key):
        """
        Add the years represented by key to the years to process.
        """
        if self._processed_data:
            message = """
                The data for this model has already been processed.
                If you would like to analyze another time period,
                then instantiate another MarchandModel instance.
            """
            raise MarchandModelError(message)

        if isinstance(key, int):
            self.years.add(key)
        elif isinstance(key, slice):
            start = key.start
            stop = key.stop
            step = key.step if key.step else 1
            self.years |= {year for year in range(start, stop, step)}
        else:
            raise TypeError("Expecting an int or slice object.")

    def process_data(self):
        pass

    def shock(self, epicenter, magnitude, weighting):
        pass

    def render(self, title):
        pass

    def list_food_balance_sheet_items(self):
        pass


class MarchandModelCommodity:
    pass

class MarchandModelBuilder:


    def __init__(self):
        self.aggregate_countries = {}
        self.network_initializers = []
        self.static_params = {}
        self.dynamic_params = {}


    # Core functionality.

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
        network.aggregated_codes = {}

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


    # Convenience functions.

    def setup_base_model(self):
        """ Set up the base model. """
        self.network_initializers[:0] = [MarchandModelBuilder.base_initializer]

    def aggregate_country_codes(self, name, country_codes):
        """ Add aggregate country to the builder. """
        self.aggregate_countries[name] = country_codes


    @staticmethod
    def base_initializer(network):
        pass
