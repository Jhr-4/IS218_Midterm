from app.commands import Command
from calculator import Calculator

class MultiplyCommand(Command):
    def execute(self, a, b):
        calculate = Calculator.multiply(a, b)
        print("The result of " + str(a) + " * " + str(b) + " is " + str(calculate))