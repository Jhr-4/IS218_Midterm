from decimal import Decimal, InvalidOperation
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def registerCommand(self, commandStr: str, command: Command):
        self.commands[commandStr] = command

    def executeCommand(self, commandStr: str, operands: str): 
        try:
            command = self.commands[commandStr] 
            if operands:
                a = Decimal(operands[0])
                b = Decimal(operands[1])
                command.execute(a, b) # the actual commands print to terminal
            else:
                command.execute() 
                
        except KeyError:
            print(f"Invalid Command: {commandStr}, Use 'menu' for commands.")
        except ZeroDivisionError as e:
           print(e) #error from divison 
        except InvalidOperation:
            print(f"Invalid Operands: {operands[0]} or {operands[1]} is not a valid number.")