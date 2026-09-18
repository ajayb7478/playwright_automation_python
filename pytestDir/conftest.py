import pytest

@pytest.fixture(scope="session") #module and class almost same runs only once in the file

# setting scope as session will make it run once per entire test execution.
def preSetupWork():
    print("I setup browser Instance for third")