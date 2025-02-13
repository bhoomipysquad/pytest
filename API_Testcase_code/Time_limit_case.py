import time

def test_execution_time():
    start_time = time.time()
    # Code you want to test
    time.sleep(1)
    assert time.time() - start_time < 2  # Test if execution time is under 2 seconds
