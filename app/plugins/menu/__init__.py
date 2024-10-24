from app.commands import Command
import logging

class MenuCommand(Command):
    def execute(self):
        logging.info(f"Used Command Menu.")
        print("Commands:\
              \n- menu: This commands menu. \
              \n- exit: Exit the app. \
              \n- add <operand1> <operand2>: Add two numbers.\
              \n- subtract <operand1> <operand2>: Subtract two numbers.\
              \n- multiply <operand1> <operand2>: Multiply two numbers. \
              \n- divide <operand1> <operand2>: Divide two numbers.")