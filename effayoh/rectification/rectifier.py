"""
Provides the PoliticalRectifier class.

"""


class DSDWholePE:
    """
    Represents a data-source defined political entity that is in itself
    a model political entity.

    """
    pass


class DSDComponentPE:
    """
    Represents a data-source defined political entity that is a
    component, along with several other data-source defined political
    entites from the same data source, a compound political entity.

    """
    pass


class DSDComponentPEGroup:
    """
    Represents a group of DSDComponentPE that comprise a whole model
    political entity.

    """
    pass


class DSDCompoundPE:
    """
    Represents a data-source defined political entity that is comprised
    of two or more model political entities (MPEs). The CompoundDSDPE
    must be split into its constituent MPEs and its data must be
    apportioned between them.

    """
    pass


class InterDataSourceMapping:
    """
    Represents a mapping of political entities from one data source to another.

    """
    pass


class PoliticalRectifier:

    def __init__(self, network, data_to_model_map):
        """
        Params:

        network:
            The NetworkX graph instance that is the network of the
            Marchand Model.

        data_to_model_map:
            A dict that maps data-source defined political entities to
            their corresponding effayoh political entity.

        """
        self.network = network
        self.data_to_model_map = data_to_model_map

    def set_network_edge(self, source, dest, name, val):
        """
        Rectify and add the edge name with value val to the network.
        """
        # The political rectifier (PR) first determines the types of
        # source and dest.
        pass

    def set_network_node_attr(self, target, name, value):
        """
        Add the distributed attribute name to the rectified target node.
        """
        # The political rectifier (PR) needs to determine what type of
        # political entity target is.
        #
        # If the political entity PE is a whole, then the PR can look up
        # the corresponding node and set its attribute.
        #
        # If the PE is a compound then the PR has to look up its
        # disaggregated nodes and apportion value among them.
        #
        # If the PE is a component, then the PR should accumulate value
        # in the corresponding node.
        pass

    def register_dsd_component_group(self, group):
        pass

    def register_dsd_compound(self, compound):
        pass
