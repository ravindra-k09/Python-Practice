import pytest

@pytest.fixture
def f1():
    print("fixture1 Message")


def test_one(f1):
    print("one")
def test_two(fixture2):
    print("two")
def test_three(f1):
    print("three")