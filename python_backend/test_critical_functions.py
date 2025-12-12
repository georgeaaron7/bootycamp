import pytest
from critical_functions import add, multiply

def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(2, 3) == 6