
import pytest

@pytest.mark.regression
def test_reg1():
    assert 1+3==4

@pytest.mark.smoke
def test_reg2():
    assert 1 + 1 == 2

@pytest.mark.sanity
def test_reg3():
    assert 1 + 1 == 2

@pytest.mark.sanity
def test_reg4():
    assert 1 + 1 == 2