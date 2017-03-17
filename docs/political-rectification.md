# Political Rectification

Political rectification refers to the process of adjusting the political
entities in the raw data to match the actual political entities in existence
over time.

Political rectification is made up of two stages. Data-source-wise political
rectification and inter-source political matching. The former manages the
merges and splits of political entities over time within the data from one
source and the latter matches the rectified entities from different data
sources.

# Data-Source-Defined Political Entity Type

Fortunately we don't have to solve the much more difficult problem of tracing
the lineage and evolution of political entities over the entire time period of
the data. For the model runs, the experiment designers will have to fix a time
period which will typically be much smaller than the data time period. Within
that time period, for each data-source defined political entity (PE), the
designer has to decide the PE's **type** which can be one of three things: the
PE is a **whole** entity, the PE is a **component** of an compound political
entity, or the PE is a **compound** political entity that is to be split up in
some way for the model.

## Type Resolution

All data-source defined political entities have an implicit type of **whole**.

If a PE has a type other than **whole** this must be declared.

A PE declared of type **component** must be registered with its **component
group**.

A PE declared of type **compound** must declare its component model political
entites (MPEs) as well as a distribution function for distributing its data
among its MPEs.

# Inter Data-Source Political Entity Reconciliation

The political rectifier will not attempt to guess at the mapping between
data-source defined political entities to model entities. The mapping must be
explicitly defined.

How and where should this mapping be defined? How should the political
rectifier fetch the mapping?

It should be defined in any module.
