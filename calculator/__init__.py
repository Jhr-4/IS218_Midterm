from calculator.History import History
from decimal import Decimal
from typing import Callable


class Calculator:

#_execute calculates and adds to history 
    def _execute(a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal],Decimal]):
        result = operation(a, b)
        History.appendHistory(a, b, operation, result)
        return result

#Operations called by user

    @staticmethod
    def add(a: Decimal, b:Decimal) -> Decimal:
        return Calculator._execute(a, b, Calculator._add)

    @staticmethod
    def subtract(a: Decimal, b:Decimal) -> Decimal:
        return Calculator._execute(a, b, Calculator._subtract)
    
    @staticmethod
    def multiply(a: Decimal, b:Decimal) -> Decimal:
        return Calculator._execute(a, b, Calculator._multiply)


    @staticmethod
    def divide(a: Decimal, b:Decimal) -> Decimal:
        return Calculator._execute(a, b, Calculator._divide)
    

#Direct Operations Only called by _perform 

    @staticmethod
    def _add(a: Decimal, b: Decimal) -> Decimal:
        return a+b
    
    @staticmethod
    def _subtract(a: Decimal, b: Decimal) -> Decimal:
        return a-b
    
    @staticmethod
    def _multiply(a: Decimal, b: Decimal) -> Decimal:
        return a*b
    
    @staticmethod
    def _divide(a: Decimal, b: Decimal) -> Decimal:
        if b == 0:
            raise ZeroDivisionError("Division by 0: Undefined")
        return a/b      