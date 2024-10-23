from app.commands import Command
from calculator import Calculator

class SubtractCommand(Command):
    def execute(self, a, b):
        calculate = Calculator.subtract(a, b)
        print("The result of " + str(a) + " - " + str(b) + " is " + str(calculate))