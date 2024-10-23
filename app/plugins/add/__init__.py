from app.commands import Command
from calculator import Calculator

class AddCommand(Command):
    def execute(self, a, b):
        calculate = Calculator.add(a, b)
        print("The result of " + str(a) + " + " + str(b) + " is " + str(calculate))