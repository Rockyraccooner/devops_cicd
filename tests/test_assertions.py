import pytest

def test_equals():
    assert 2 == 2

def test_greaterthan():
    assert 2 > 1

def test_lessthen():
    assert 1 < 2

def test_notequalto():
    assert 1 != 2

def test_greaterorequal():
    assert 3 >= 3

def test_lessorequal():
    assert 2 <= 2

def test_tupleequals():
    assert (1,2) == (1,2)

def test_elementinlist():
    assert 2 in [1, 2]

def test_equalsstring():
    string1 = "abc"
    string2 = "abc"
    assert(string1 == string2)
