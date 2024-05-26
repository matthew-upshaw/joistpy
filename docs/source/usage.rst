Usage
=====

.. _installation:

Installation
------------

To use JoistPy, first install it using pip:

.. code-block:: bash

	pip install joistpy

To access the properties within the library, 
first import the module.

.. code-block:: python

	from joistpy import sji

The library includes all standard K, LH, and
DLH joist designations. To access the K-Series
joists, for example, use dot notation for the 
group of designations.

.. code-block:: python

	sji.K_Series

From there specific designations can be obtained 
in a similar manner. Note that the prefix K,
LH, or DLH followed by an underscore must be added to the joist
designation in order to properly access it via 
dot notation.

.. code-block:: python

	joist = sji.K_Series.K_8K1

Properties can be obtained in a similar manner. 
Properties that can be accessed include approximate 
weight in plf and load tables for L/360 deflection
criteria and Total Safe Load. Span values are in ft
and load table values are in plf.

.. code-block:: python

	weight = joist.weight
	l360 = joist.l360
	total = joist.total

Additonal properties can be calculated by using the 
Designation class methods.

.. code-block:: python

	span = 17.5 # joist span in ft
	area = joist.get_eq_area() # equivalent cross-sectional are in in^2
	mom_inertia = joist.get_mom_inertia(span) # moment of inertia in in^4
	wl360 = joist.get_wl360(span) # load that produced L/360 deflection for the span in plf
