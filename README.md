# JoistPy

JoistPy is a library that acts as a database for SJI steel open web bar joist shapes for easy use in structural calculations.

## Contents
* [Installation](#installation)
* [Usage](#usage)
* [get_mom_inertia Method](#get_mom_interta-method)

## Installation
Install using pip:
```
pip install joistpy
```

## Usage
To use the joistpy library, first import the module

```
from steelpy import sji
```

The library includes all standard K-Series joist designations. To access the K-Series joists, use dot notation for the group of designations:
```
sji.K_Series
```

From there specific designations can be obtained in a similar manner. Note that the prefix 'K_' must be added to the joist designation in order to properly access it via dot notation:
```
joist = sji.K_Series.K_8K1
```

Properties can be obtained in a similar manner. Properties that can be accessed include approximate weight in plf and load tables for L/360 deflection criteria and Total Safe Load. Span values are in ft and load table values are in plf:
```
joist = sji.K_Series.K_8K1
weight = joist.weight
l360 = joist.l_360
total = joist.total
```

## get_mom_inertia Method
The `get_mom_inertia` method allows you to quickly calculate the moment of inertia for your joist and given span.
```
joist = sji.K_Series.K_12K1
span = 22.5
Ix = joist.get_mom_inertia(span=span)
```