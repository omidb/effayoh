"""
Provide the MarchandModel class.

"""

import networkx as nx

from effayoh.rectification.rectifier import PoliticalRectifier


class MarchandModelError(Exception): pass


class MarchandModel:

    """
    A model of global trade shock dynamics.

    The Marchand model is a model of the behavior of the global food
    trade network when a production shock occurs in one country.
    Rules are applied to propagate the shock and distribute the loss in
    production throughout the trade network.

    """

    def __init__(self,
                 static_params,
                 dynamic_params,
                 policy,
                 politent_maps,
                 builder):
        self.network = nx.DiGraph()
        self.static_params = static_params
        self.dynamic_params = dynamic_params
        self.policy = policy
        self.builder = builder
        self.political_rectifier = PoliticalRectifier(self.network,
                                                      politent_maps)

    def get_political_rectifier(self):
        return self.political_rectifier

    def run(self, iterations=100):
        pass

    def step(self):
        pass

    def update_params(self):
        pass
