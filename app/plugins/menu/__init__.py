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
              \n- divide <operand1> <operand2>: Divide two numbers.\
              \n- peekHistory <optional:#>: Get '#' Most Recent Calculations (Default=5).\
              \n- clearHistory: Clear History.\
              \n- saveHistory <name>: Save History to .csv of name <name> in ./data folder. Warning using duplicate names will replace the file.\
              \n- loadHistory <name>: Load History of name <name>.csv. Must be ./data folder and in correct format of operands, operator, and result.")