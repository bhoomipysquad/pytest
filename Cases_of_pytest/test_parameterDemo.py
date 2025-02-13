import pytest


@pytest.mark.parametrize("name,roll,city",[("riya",3,"ahm"),("priya",3,"meh")])
def test_validation(name,roll,city):
    assert name != None
    assert roll != None
    assert city != None
    print(name,roll,city)

@pytest.fixture(scope="module",params=["www.google.com","www.amazon.com","www.flipkart.com"])
def val(request):
    return request.param    #this is the fixture which will run in module

def test_val(val):
    assert val != None



