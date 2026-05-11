from src.main import Calculator

def test_divide():
    x = 1
    y = 2
    res = 0.5
    assert Calculator(x,y).divide() == res