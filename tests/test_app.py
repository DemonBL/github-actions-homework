import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from myapp.app import add, subtract

def test_add():
    """Tests the addition function."""
    assert add(2, 3) == 5

def test_subtract():
    """Tests the subtraction function."""
    assert subtract(5, 3) == 2