from shop_app.calculator import Calculator

def test_add():
    assert Calculator.add(1, 1) == 2

def test_add_negative_ones():
    assert Calculator.add(-1, -1) == -2

def test_times():
    assert Calculator.times(2, 4) == 8

def test_divider():
    assert Calculator.divider(3, 2) == 1.5

def test_class():
    calc = Calculator()
    assert calc