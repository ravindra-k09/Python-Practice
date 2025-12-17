import pytest

test_data = [
    (1, 1),
    (2, 4),
    (3, 9),
    (4, 16),
]

@pytest.mark.parametrize("input, output", test_data)
def test_squareroot(input, output):
    assert input**2 ==output
    
# @pytest.mark.parametrize("input, output", test_data)
# def test_add(input, output):
#     assert input+input==output