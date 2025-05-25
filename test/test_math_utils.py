from src.math_utils import add, divide


def test_add():
    assert add(1, 10) == 11
    assert add(2, 20) == 22


def test_add2():
    assert add(100, 10) == 110
    assert add(24, 220) == 224


def test_divide():
    assert divide(1, 10) == 0.1
    assert divide(2, 20) == 0.1
