import pytest

from joistpy import Designation, sji

k_14k1 = sji.K_Series.K_14K1

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

def test_get_mom_inertia():
    k_14k1.get_mom_inertia()

def test_get_wl360_valid_span():
    k_14k1.get_wl360(span=15)

def test_get_wl360_invalid_span():
    k_14k1.get_wl360(span=-1)

def test_get_wl360_invalid_span_type():
    with pytest.raises(TypeError):
        k_14k1.get_wl360('5')

def test_get_wtotal_valid_span():
    k_14k1.get_wtotal(span=15)

def test_get_wtotal_invalid_span():
    k_14k1.get_total(span=-1)

def test_get_wtotal_invalid_span_type():
    with pytest.raises(TypeError):
        k_14k1.get_wtotal('5')

