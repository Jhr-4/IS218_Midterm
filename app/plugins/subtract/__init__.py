from app.commands import Command
from calculator import Calculator
import logging

class SubtractCommand(Command):
    def execute(self, a, b):
        calculate = Calculator.subtract(a, b)
        logging.info(f"Used Command Subtract: {a} - {b} = {calculate}.")
        print("The result of " + str(a) + " - " + str(b) + " is " + str(calculate))