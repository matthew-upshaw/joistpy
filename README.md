<p align="center">
    <a href="https://github.com/matthew-upshaw/joistpy/actions/workflows/tests.yml"><img alt="Tests" src="https://github.com/matthew-upshaw/joistpy/actions/workflows/tests.yaml/badge.svg"></a>&nbsp;&nbsp;&nbsp;
    <a href="https://coveralls.io/github/matthew-upshaw/joistpy?branch=main"><img alt="Coverage Status" src="https://coveralls.io/repos/github/matthew-upshaw/joistpy/badge.svg?branch=main&v=0.1.2"></a>&nbsp;&nbsp;&nbsp;
    <a href="https://github.com/matthew-upshaw/joistpy/blob/main/LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>&nbsp;&nbsp;&nbsp;
</p>

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

The library includes all standard K-, and KCS-Series joist designations. To access the K-Series joists use dot notation for the group of designations.
```python
sji.K_Series
```

The KCS-Series joists can be accessed in a similar fashion.

From there specific designations can be obtained in a similar manner. Note that the prefix 'K_' or 'KCS_', as applicable, must be added to the joist designation in order to properly access it via dot notation.
```python
k_joist = sji.K_Series.K_8K1
kcs_joist = sji.KCS_Series.KCS_14KCS1
```

Properties can be obtained in a similar manner. Properties that can be accessed include approximate weight in plf and load tables for L/360 deflection criteria and Total Safe Load. Span values are in ft and load table values are in plf. Shear capacity in lbs can also be accessed for KCS joists.
```python
weight = k_joist.weight
l360 = k_joist.l_360
total = k_joist.total
shear_capacity = kcs_joist.shear_capacity
```

Additonal properties can be calculated by using the Designation class methods.
```python
span = 17.5 # joist span in ft
area = joist.get_eq_area() # equivalent cross-sectional are in in^2
mom_inertia = joist.get_mom_inertia(span) # moment of inertia in in^4
wl360 = joist.get_wl360(span) # load that produced L/360 deflection for the span in plf
```

### Additional Information
- [Documentation](https://joistpy.readthedocs.io/en/latest/index.html)
- [PyPI Release](https://pypi.org/project/joistpy/)
