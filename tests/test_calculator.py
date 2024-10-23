from decimal import Decimal
import pytest
from calculator import Calculator

@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('50'), Decimal('50'), Calculator.add, Decimal('100')),
    (Decimal('50.1'), Decimal('50'), Calculator.add, Decimal('100.1')),
    (Decimal('10'), Decimal('50'), Calculator.subtract, Decimal('-40')),
    (Decimal('50'), Decimal('10.1'), Calculator.subtract, Decimal('39.9')),
    (Decimal('30'), Decimal('10'), Calculator.multiply, Decimal('300')),
    (Decimal('3.14'), Decimal('1'), Calculator.multiply, Decimal('3.14')),
    (Decimal('50'), Decimal('50'), Calculator.divide, Decimal('1')),
    (Decimal('100'), Decimal('50'), Calculator.divide, Decimal('2')),
])

def test_calculator(a, b, operation, expected):
    assert operation(a, b) == expected

def test_division_0():
    with pytest.raises(ZeroDivisionError, match="Division by 0: Undefined"):
        Calculator.divide(Decimal('50'), Decimal('0'))