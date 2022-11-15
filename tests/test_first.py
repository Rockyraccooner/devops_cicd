import pytest

def test_hello_world():
    print("I'm printing hello world")

def test_upper():
    assert 'foo'.upper() == 'FOO'
