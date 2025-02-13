import sys
import pytest

@pytest.mark.skipif(sys.version_info < (3, 6), reason="Requires Python 3.6+")
def test_python_version():
    assert True
