"""
Provides the PoliticalRectifier class.

"""


class WholePoliticalEntity:
    """
    An effayoh political entity that is in itself a network node.

    """
    pass


class ComponentPoliticalEntity:
    """
    An effayoh political entity that is one of two or more effayoh
    political entities that comprise a network node.

    """
    pass


class ComponentPoliticalEntityGroup:
    """
    A group of effayoh political entities that comprise a network node.

    """
    pass


class CompoundPoliticalEntity:
    """
    An effayoh political entity that comprises two or more network
    nodes.

    The CompoundPoliticalEntity must be split into its comprising
    nodes and its data must be apportioned between them.

    """
    pass


class PoliticalRectifier:

    def __init__(self, network):
        """
        Params:

        network:
            The NetworkX graph instance that is the network of the
            Marchand Model.

        """
        self.network = network
        # TODO: Get data-source defined political entity to effayoh
        # political entity maps.

    def set_network_edge(self, source, dest, name, val):
        """
        Rectify and add the edge name with value val to the network.
        """
        # Determine the data source from which source and dest
        # originate.
        #
        # Map source and dest to their effayoh political entities.
        pass

    def set_network_node_attr(self, target, name, value):
        """
        Add the distributed attribute name to the rectified target node.
        """
        # Determine from which data source this data originates.
        #
        # Map target to its effayoh political entity.
        #
        # Look up the type of the effayoh political entity.
        #
        # If it is a Whole, look up its node and set the node's
        # attribute.
        #
        # If it is a compound, look up its nodes and apportion value
        # between them.
        #
        # If it is a component, look up its corresponding node and
        # accumulate value.
        pass

    def register_effayoh_component_group(self, group):
        pass

    def register_effayoh_compound_pe(self, compound):
        pass
