#Fixtures

import pytest

@pytest.fixture(scope="module") #module and class almost same runs only once in the file
def preWork():
    print("I setup browser module Instance")
    return "I am preWork pass"

def test_initialCheck(preWork):
    print("this is first test")
    assert preWork == "I am preWork pass"

def test_SecondCheck(preWork):
    print("This is second test")

@pytest.fixture(scope="function") #module and class almost same runs only once in the file
def secondWork():
    print("I setup browser function Instance")
    yield
    print("I tear down browser function Instance")

def test_ThirdCheck(preWork, secondWork):
    print("this is third test")
    assert preWork == "I am preWork pass"