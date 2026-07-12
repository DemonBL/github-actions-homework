from myapp.app import add, subtract

def test_add():
    """Tests the addition function."""
    assert add(2, 3) == 5

def test_subtract():
    """Tests the subtraction function."""
    assert subtract(5, 3) == 2