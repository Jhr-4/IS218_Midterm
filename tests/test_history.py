from decimal import Decimal
import pytest
from calculator import History
from calculator import Calculator


@pytest.fixture
def setup():
    History.clearHistory()
    History.appendHistory(Decimal('10'), Decimal('4'), Calculator.add, Decimal('14'))
    History.appendHistory(Decimal('30'), Decimal('.5'), Calculator.subtract, Decimal('29.5'))

def test_history(setup):
    assert History.getLatest() == (Decimal('30'), Decimal('.5'), "subtract", Decimal('29.5')), "Append History Broken" # check append History
    Calculator.add(Decimal('10'), Decimal('100'))
    assert History.getLatest() == (Decimal('10'), Decimal('100'), "add", Decimal('110')), "Direct Calculation to History Broken"

def test_history_clear(setup):
    History.clearHistory()
    assert len(History.getHistory()) == 0, "History Clear Broken"