import pytest


@pytest.mark.xfail
def test_buggy_code():
    assert 1 + 1 == 3  # This will fail, but is expected
