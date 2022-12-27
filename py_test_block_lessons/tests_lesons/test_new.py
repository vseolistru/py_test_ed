import pytest

@pytest.fixture()
def some_func():
    print('fixture are loading')

def test_hello(some_func):
    print('Hello')

def test_world(some_func):
    print('world')