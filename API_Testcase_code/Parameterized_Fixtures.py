import pytest

@pytest.fixture(params=[1, 2, 3])
def number(request):
    return request.param

def test_multiply_by_two(number):
    assert number * 2 == number + number
