import print
import pytest


def test_nameNotEmpty():
    name = ""

    with pytest.raises(Exception):
        print.hello(name)

def test_nameLengh():
    name = "azertyuiopqsdfghjklmwxcvbnazeaa"

    with pytest.raises(Exception):
        print.hello(name)


def test_hello():
    name = "Théo"

    result = print.hello(name)
    
    assert result == "Hello Théo"