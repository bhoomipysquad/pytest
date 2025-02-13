import pytest

@pytest.fixture
def data():
    return 5

def test_add(data):
    result = data + 3
    assert result == 8

def test_addd(data):
    result = data - 3
    assert result == 7
