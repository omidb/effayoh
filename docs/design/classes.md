# effayoh classes

This file documents the effayoh classes.

1. The MarchandModel class implements the Marchand model.
1. The MarchandModelBuilder class.
3. The `MarchandModelCommodity` class represents the commodity that forms the
   trade network at the heart of the Marchand model. The MarchandModelCommodity
   class synthesizes the information

# Marchand Model

The Marchand Model is a representation of the dynamics of the global food trade
system under shock.

## Functionality

1. Specify what commodity will from the basis of the network. The different
   types of commodity that can be specified are:

   - FAO Atomic: a commodity that corresponds to exactly 1 item from the FAO
     food balance sheet definition and standard. This can be specified by
     either the value of the item code or item fields in the food balance
     sheets definitions and standards.
   - MarchandModelCommodity subclass: a commodity that does not correspond to
     exactly 1 item from the FAO food balance sheet definition and standards.
     The user must define a subclass of MarchandModelCommodity that knows how
     to produce the information needed by the MarchandModel to operate.

2. Specify the time period that the model should consider. This can be done by:

   - Passing in a collection of integers.
   - Passing a slice object to the \_\_getitem\_\_ method.

3. Set model global parameters.
4. Set individual values on the underlying NetworkX graph.
5. Conveniently specify a distribution of reserves, production, consumption,
   imports and exports.
6. Build the model from a file.
7. Add dynamic global variables (price for example).
8. Allow for custom policy creation, for example creating a new policy that
   redistributes based on price, so the policy needs to be able to examine
   the state of individual nodes in the network as well as global variables.

   Perhaps it would be better to have a Builder class for the MarchandModel.

   The intent of the builder pattern in the big 4's seminal work is:

        Separate the construction of a complex object from its representation
        so that the same construction process can create different
        representations.

   This is exactly what the doctor ordered. The builder class should allow for
   the addition of global variables that are derived from system state and in
   turn affect system state.

   ```python
   from effayoh.common.marchandmodel import MarchandModelBuilder

   from custom_package import price, node_update_policy

   builder = MarchandModelBuilder()
   builder.setup_base_model()
   builder.define_dynamic_global_state_variable("price", price)

   builder.set_update_policy(update_policy)
   ```

   ```python
   def update_policy(epicenter, shock, network, globals_):
       delta_reserves = max(0, globals_.fr*node.reserves)
       if delta_reserves:
         node.reserves -= delta_reserves

       ...

       # Do something with price
       price = globals_.price
       # Stuff
   ```

# Marchand Model Builder

- global state variables.
- node initialization variables.

## Functionality

1. Add node attribute (reserves).
2. Add network initializer (MarchandModelCommodity).
3. Add static model parameter.
4. Add dynamic model parameter.
5. Set update policy.

For the price you need to add a global computed attribute.

Possible optional functionality:

1. add edge generator.

## FAO Data Sheet Requirements

The Marchand model requires information from the detailed trade matrix data
sheet and the food balance data sheet.

1. Trade volumes for the atomic or aggregate item under consideration derived
   from the detailed trade matrix.
2. Production, reserves and consumption from the food balance sheet.
