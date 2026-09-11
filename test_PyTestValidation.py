#Fixtures

import pytest

@pytest.fixture(scope="module") #module and class almost same runs only once in the file


def preWork():
    print("I setup browser module Instance")

def test_initialCheck(preWork):
    print("this is first test")

def test_SecondCheck(preWork):
    print("This is second test")
