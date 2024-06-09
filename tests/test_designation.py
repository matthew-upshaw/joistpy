import pytest

from joistpy import Designation, sji

k_14k1 = sji.K_Series.K_14K1
kcs_14kcs1 = sji.KCS_Series.KCS_14KCS1

@pytest.fixture
def joist_test():
    return Designation('K_14K1')

def test_designation_initialization(joist_test):
    assert joist_test.name == 'K_14K1'
    assert joist_test.properties == {}

def test_invalid_property(joist_test):
    with pytest.raises(AttributeError):
        joist_test.weight

def test_add_property(joist_test):
    joist_test._add_property(name='weight', value=5)

def test_get_eq_area():
    k_14k1.get_eq_area()
    kcs_14kcs1.get_eq_area()

def test_get_mom_inertia():
    k_14k1.get_mom_inertia(span=15)
    kcs_14kcs1.get_mom_inertia(span=15)

def test_get_wl360_valid_span():
    k_14k1.get_wl360(span=15)
    kcs_14kcs1.get_wl360(span=15)

def test_get_wl360_invalid_span_low():
    k_14k1.get_wl360(span=-5)
    kcs_14kcs1.get_wl360(span=-5)

def test_get_wl360_invalid_span_high():
    k_14k1.get_wl360(span=70)
    kcs_14kcs1.get_wl360(span=70)

def test_get_wl360_invalid_span_type():
    with pytest.raises(TypeError):
        k_14k1.get_wl360(span='5')

def test_get_wtotal_valid_span():
    k_14k1.get_wtotal(span=15)
    kcs_14kcs1.get_wtotal(span=15)

def test_get_wtotal_invalid_span_low():
    k_14k1.get_wtotal(span=-5)
    kcs_14kcs1.get_wtotal(span=-5)

def test_get_wtotal_invalid_span_high():
    k_14k1.get_wtotal(span=70)
    kcs_14kcs1.get_wtotal(span=70)

def test_get_wtotal_invalid_span_type():
    with pytest.raises(TypeError):
        k_14k1.get_wtotal(span='5')

def test_kcs_shear_capacity():
    assert kcs_14kcs1.shear_capacity == 2900

