from decimal import Decimal, InvalidOperation
from abc import ABC, abstractmethod
import logging

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def registerCommand(self, commandStr: str, command: Command):
        self.commands[commandStr] = command

    def executeCommand(self, commandStr: str, args: str): 
        try:
            command = self.commands[commandStr] 
            if args:
                if len(args) == 1:
                    a = args[0]
                    command.execute(a)
                else:
                    a = Decimal(args[0])
                    b = Decimal(args[1])
                    command.execute(a, b) # the actual commands print to terminal
            else:
                command.execute() 
                
        except KeyError:
            logging.warning(f"Invalid Command: {commandStr} was attempted.") 
            print(f"Invalid Command: {commandStr}, Use 'menu' for commands.")
        except ZeroDivisionError as e:
            logging.info(f"Division by 0.") 
            print(e) #error from divison 
        except ValueError as e:
            logging.info(f"Invalid arguments used '{args[0]}'.") 
            print(f"Invalid arguments used '{args[0]}.' Use 'menu' to see formating.") #error from divison 
        except FileNotFoundError as e:
            print(e) #error handled in history commands
        except InvalidOperation:
            logging.warning(f"Invalid Operands: '{args[0]}' and '{args[1]}' were used.")
            print(f"Invalid Operands: {args[0]} or {args[1]} is not a valid number.")