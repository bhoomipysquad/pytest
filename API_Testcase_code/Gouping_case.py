import pytest

@pytest.mark.slow
def test_long_running_task():
    assert True

@pytest.mark.fast
def test_fast_task():
    assert True
