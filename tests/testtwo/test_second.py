import pytest

def test_second():
    print("second")

def test_isupper():
    assert 'FOO'.isupper() == True
    assert 'Foo'.isupper() == False
