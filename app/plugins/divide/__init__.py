from app.commands import Command
from calculator import Calculator
import logging

class DivideCommand(Command):
    def execute(self, a, b):
        calculate = Calculator.divide(a, b)
        logging.info(f"Used Command Divide: {a} / {b} = {calculate}.")
        print("The result of " + str(a) + " / " + str(b) + " is " + str(calculate))