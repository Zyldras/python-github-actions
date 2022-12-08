# content of test_sample.py
import pytest
import print as print

def test_nameNotEmpty():
    try:
        print.hello("")
    except Exception as e:
        assert False, f"Nope {e}"

def test_nameLengh():
    try:
        print.hello("azertyuiopqsdfghjklmwxcvbnazera")
    except Exception as e:
        assert False, f"Nope {e}"

def test_hello():
    assert print.hello("Tho") == "Hello Théo"