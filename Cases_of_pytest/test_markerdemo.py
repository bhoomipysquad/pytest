import pytest

@pytest.mark.regression
def test_regression():
    print("test 1")

@pytest.mark.xfail
def test_regression4():
    print("test 2")
    assert 5==4

@pytest.mark.regression
def test_regression1():
    print("test 1")

@pytest.mark.sanity
def test_sanity1():
    print("test 1")

@pytest.mark.skip
def test_skip():
    print("test 1")