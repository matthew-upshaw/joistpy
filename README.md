# JoistPy

JoistPy is a library that acts as a database for SJI steel open web bar joist shapes for easy use in structural calculations.

### Installation
Install using pip:
```
pip install joistpy
```

### Usage
To use the joistpy library, first import the module

```python
from joistpy import sji
```

The library includes all standard K-Series joist designations. To access the K-Series joists use dot notation for the group of designations.
```python
sji.K_Series
```

From there specific designations can be obtained in a similar manner. Note that the prefix 'K_' must be added to the joist designation in order to properly access it via dot notation.
```python
joist = sji.K_Series.K_8K1
```

Properties can be obtained in a similar manner. Properties that can be accessed include approximate weight in plf and load tables for L/360 deflection criteria and Total Safe Load. Span values are in ft and load table values are in plf.
```python
weight = joist.weight
l360 = joist.l_360
total = joist.total
```

Additonal properties can be calculated by using the Designation class methods.
```python
span = 17.5 # joist span in ft
area = joist.get_eq_area() # equivalent cross-sectional are in in^2
mom_inertia = joist.get_mom_inertia(span) # moment of inertia in in^4
wl360 = joist.get_wl360(span) # load that produced L/360 deflection for the span in plf
```
