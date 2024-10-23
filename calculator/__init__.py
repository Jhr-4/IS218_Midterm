from calculator.History import History
from decimal import Decimal


class Calculator:

    @staticmethod
    def add(a: Decimal, b:Decimal) -> Decimal:
        result = a+b
        History.appendHistory(a, b, Calculator.add, result)
        return result

    @staticmethod
    def subtract(a: Decimal, b:Decimal) -> Decimal:
        result = a-b
        History.appendHistory(a, b, Calculator.subtract, result)
        return result
    
    @staticmethod
    def multiply(a: Decimal, b:Decimal) -> Decimal:
        result = a*b
        History.appendHistory(a, b, Calculator.multiply, result)
        return result


    @staticmethod
    def divide(a: Decimal, b:Decimal) -> Decimal:
        if b == 0:
            raise ZeroDivisionError("Division by 0: Undefined")
        result = a/b
        History.appendHistory(a, b, Calculator.divide, result)
        return result