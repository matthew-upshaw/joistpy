import pytest

from joistpy import Joist

@pytest.fixture
def sji_test():
    return Joist('sji')

def test_joist_initialization(sji_test):
    assert sji_test.name == 'sji'
    assert sji_test.joist_type == {}

def test_invalid_attribute(sji_test):
    with pytest.raises(AttributeError):
        sji_test.LH

def test_add_joist_type(sji_test):
    sji_test._add_joist_type('K', ['Collection'])
