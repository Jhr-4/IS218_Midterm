from app.commands import Command
from calculator import Calculator
import logging

class AddCommand(Command):
    def execute(self, a, b):
        calculate = Calculator.add(a, b)
        logging.info(f"Used Command Add: {a} + {b} = {calculate}.")
        print("The result of " + str(a) + " + " + str(b) + " is " + str(calculate))