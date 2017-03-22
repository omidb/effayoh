"""
Provides the PoliticalRectifier class.

"""
from effayoh.rectification.political_entities import FAOPolitEnt


class RectificationError(Exception): pass


class ModelPolitent: pass


class WholePoliticalEntity(ModelPolitent):
    """
    An effayoh political entity that is in itself a network node.

    """

    def __init__(self, effpent):
        self.name = effpent.name
        self.value = effpent.value


class CompoundPoliticalEntity(ModelPolitent):
    """
    An effayoh political entity that comprises two or more network
    nodes.

    The CompoundPoliticalEntity must be split into its comprising
    nodes and its data must be apportioned between them.

    """

    def __init__(self, effpent, constituent_names, distribution):
        self.effpent = effpent
        self.constituent_names = constituent_names
        self.distribution = distribution
        # The constituents dict attribute is populated when the
        # CompoundPoliticalEntity instance is registered with a
        # PoliticalRectifier.
        self.constituents = {}

    def scale(self, constituent_name, value):
        """
        Return value scaled by the portion assigned to constituent_name.
        """
        numerator = self.distribution[constituent_name]
        denominator = sum(self.distribution.values())
        return value*numerator / denominator

    def distribute_node_attr(self, name, value):
        """
        Distribute value among the nodes that comprise this political
        entity.
        """
        for cname, node in self.constituents.items():
            scale = self.scale(cname, value)
            node[name] = node.get(name, 0.0) + scale


class ComponentPoliticalEntity(ModelPolitent):
    """
    An effayoh political entity that is one of two or more effayoh
    political entities that comprise a network node.

    """
    pass


class ComponentPoliticalEntityGroup(list):
    """
    A group of effayoh political entities that comprise a network node.
    """

    def __init__(self, name, elements):
        self.name = name
        super().__init__(elements)


class PoliticalRectifier:

    def __init__(self, network, politent_maps):
        """
        Params:

        network:
            The NetworkX graph instance that is the network of the
            Marchand Model.

        politent_maps:
            A dict that maps a data source political entity to its
            effpent mapping.

        component_political_entities:
            A dict that maps component effpents to their groups.

        """
        self.network = network
        self.politent_maps = politent_maps
        self.component_political_entities = {}
        self.compound_politents = []
        self.mpent_to_node = {}
        self.effpent_to_mpent = {}

    def get_effayoh_politent(self, data_politent):
        """
        Return the associated FAOPolitEnt of data_politent.
        """
        for politent_type in self.politent_maps:
            if type(data_politent) is politent_type:
                map_ = self.politent_maps[politent_type]
                break
        else:
            msg = "Received an undefined Political Entity Type."
            raise RectificationError(msg)
        return map_[data_politent]

    def get_model_politent(self, data_politent):
        """
        Return the ModelPolitent associated to data_politent.
        """
        effpent = self.get_effayoh_politent(data_politent)
        if effpent in self.component_political_entities:
            return self.component_political_entities[effpent]
        elif effpent in self.effpent_to_mpent:
            return self.effpent_to_mpent[effpent]
        else:
            mpent = WholePoliticalEntity(effpent)
            self.effpent_to_mpent[effpent] = mpent
            return mpent

    def rectify(self, effpent):
        """
        Return the network node that represents this effpent.
        """
        mpent = self.get_model_politent(effpent)
        if not isinstance(mpent, ModelPent):
            raise RectificationError("Cannot rectify non ModelPent instance.")
        elif isinstance(mpent, CompoundPoliticalEntity):
            raise RectificationError("Cannot rectify CompoundPoliticalEntity")
        elif isinstance(mpent, ComponentPoliticalEntity):
            group = self.component_political_entities[effpent]
            return self.mpent_to_node[group]
        elif mpent in self.mpent_to_node:
            return self.mpent_to_node[mpent]
        else:
            name = mpent.name
            self.network.add_node(name)
            node = self.network[name]
            self.mpent_to_node[name] = node
            return self.mpent_to_node[name]

    def set_network_edge(self, source, dest, name, value):
        """
        Rectify and add the edge name with value to the network.
        """
        # TODO: Change effpents to mpents.
        effpent_source = self.get_effayoh_politent(source)
        effpent_dest = self.get_effayoh_politent(dest)

        if isinstance(effpent_source, CompoundPoliticalEntity) and\
           isinstance(effpent_dest, CompoundPoliticalEntity):
            _set_network_edge_compound_to_compound(
                effpent_source,
                effpent_dest,
                name,
                value
            )
        elif isinstance(effpent_source, CompoundPoliticalEntity):
            _set_network_edge_compound_source(
                effpent_source,
                effpent_dest,
                name,
                value
            )
        elif isinstance(effpent_dest, CompoundPoliticalEntity):
            _set_network_edge_compound_dest(
                effpent_source,
                effpent_dest,
                name,
                value
            )
        else:
            # Make sure that nodes exist in the graph.
            source_node = self.rectify(source)
            dest_node = self.rectify(dest)
            self.network.add_edge(source.name, dest.name, name, value)

    def _set_network_edge_compound_to_compound(self, source, dest, name, value):
        """
        For each pair of constituents value must be scaled by the
        product of their distributions.
        """
        for sname in source.constituent_names:
            sscale = source.scale(sname, value)
            for dname in dest.constituent_names:
                dscale = dest.scale(dname, sscale)
                self.network.add_edge(sname, dname, name=dscale)

    def _set_network_edge_compound_source(self, source, dest, name, value):
        if dest in self.component_political_entities:
            dst = self.component_political_entities[dest]
        for sname in source.constituent_names:
            scaled_value = source.scale(sname, value)
            self.network.add_edge(sname, dst.name, name=scaled_value)

    def _set_network_edge_compound_dest(self, source, dest, attr_name, value):
        if source in self.component_political_entities:
            src = self.component_political_entities[source]
        for dname in dest.constituent_names:
            scaled_value = dest.scale(dname, value)
            self.network.add_edge(src.name, dname, attr_name=scaled_value)

    def set_network_node_attr(self, data_politent, name, value):
        """
        Add the distributed attribute name to the rectified
        data_politent node.

        Params:

            data_politent:
                The data-source defined political entity passed in by
                the data-source specific munger.

            name:
                The name of the attribute we wish to give to the node.

            value:
                The desired value of the attribute.
        """
        # Determine from which data source this data originates.
        #
        # Map data_politent to its effayoh political entity.
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
        effpent = self.get_effayoh_politent(data_politent)
        if isinstance(effpent, WholePoliticalEntity):
            self._set_network_node_attr_whole(effpent, name, value)
        elif isinstance(effpent, ComponentPoliticalEntity):
            self._set_network_node_attr_component(effpent, name, value)
        elif isinstance(effpent, CompoundPoliticalEntity):
            self._set_network_node_attr_compound(effpent, name, value)
        else:
            raise TypeError("politent must be a political entity")

    def _set_network_node_attr_whole(self, politent, name, value):
        node = self.rectify(politent)
        if name in node:
            raise RectificationError("node already has an attribute name")
        else:
            node[name] = value

    def _set_network_node_attr_component(self, politent, name, value):
        node = self.rectify(politent)
        if name in node:
            node[name] += value
        else:
            node[name] = value

    def _set_network_node_attr_compound(self, politent, name, value):
        politent.distribute_node_attr(name, value)

    def register_effayoh_component_group(self, group):
        """
        Register the ComponentPoliticalEntityGroup group with this
        rectifier.

        Is this more complicated than saving this group in a collection
        like a list?

        What do we want to do with this in the future? We want to check
        if an effpent is in one of these component groups and if it is,
        fetch its component group.

        We also have to create a node for the component group.
        """

        for component in group:

            if component in self.component_political_entities:
                msg = ("A ComponentPoliticalEntity instance is assigned "
                       "to more than one ComponentPoliticalEntityGroup.")
                raise RectificationError(msg)

            if group.name in self.network:
                raise RectificationError("Duplicate component group names.")
            else:
                self.network.add_node(group.name)
                node = network[group.name]

            self.component_political_entities[component] = group
            self.mpent_to_node[group] = node

    def register_effayoh_compound_political_entity(self, compound):
        """
        Register compound political entity with this rectifier.

        We want to check if an effpent is a compound political entity.

        We need to set up the nodes that this compound politent
        represents.

        The CompoundPoliticalEntity must declare the names of its
        constituent model political entities and define how to
        apportion its data among them.
        """

        for name in compound.constituent_names:

            if name in self.network:
                raise RectificationError("Duplicate constituent names")
            else:
                self.network.add_node(name)
                compound.constituents[name] = self.network[name]

        else:
            self.compound_politents.append(compound)
            self.effpent_to_mpent[compound.effpent] = compound
