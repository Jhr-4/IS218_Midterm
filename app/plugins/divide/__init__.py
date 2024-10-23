from app.commands import Command
from calculator import Calculator

class DivideCommand(Command):
    def execute(self, a, b):
        calculate = Calculator.divide(a, b)
        print("The result of " + str(a) + " / " + str(b) + " is " + str(calculate))