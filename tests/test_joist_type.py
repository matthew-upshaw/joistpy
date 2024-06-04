import pytest

from joistpy import JoistType

@pytest.fixture
def k_series_test():
    return JoistType('K_Series')

def test_joist_type_initialization(k_series_test):
    assert k_series_test.name == 'K_Series'
    assert k_series_test.designations == {}

def test_invalid_attribute(k_series_test):
    with pytest.raises(AttributeError):
        k_series_test.K_14K1

def test_add_designation(k_series_test):
    k_series_test._add_designation(name='K_14K1', value=['Properties'])