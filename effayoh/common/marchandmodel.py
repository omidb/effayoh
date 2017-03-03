"""
:class MarchandModel:
    Implements the model of Marchand et al.

:class MarchandModelItem:
    Used by the MarchandModel as the basis of the trade network.
"""


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

    def setup_base_model(self):
        pass

    def add_network_initializer(self, initializer):
        pass

    def add_static_param(self, name, val):
        pass

    def add_dynamic_param(self, name, func):
        pass

    def set_update_policy(self, policy):
        pass

    def build(self, base=True):
        model = MarchandModel()
        if base:
            self.setup_base_model()
        # Add static parameters and dynamic parameters.
        model.params = self.static_params + self.dynamic_params
        # Execute initializers.
        for initializer in self.network_initializers:
            initializer(model)
        # Set the update policy.
        model.update_policy = self.update_policy
        return model
