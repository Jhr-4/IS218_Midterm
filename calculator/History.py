from decimal import Decimal
from typing import Callable

class History:
    _history: list = []

    @classmethod
    def appendHistory(cls, a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal],Decimal], result: Decimal):
        input = (a, b, operation.__name__, result)
        cls._history.append(input)

    @classmethod
    def getHistory(cls):
        return cls._history
    
    @classmethod
    def getLatest(cls):
        return cls._history[-1]
    
    @classmethod
    def clearHistory(cls):
        cls._history.clear()