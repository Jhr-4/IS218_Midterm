import os
import importlib
from app.commands import CommandHandler
from app.commands import Command


class App:
    def __init__(self):
        self.commandHandler = CommandHandler()

    def start(self):

        plugins_pkg = 'app.plugins'
        plugins_path = 'app/plugins'

        for folder in os.listdir(plugins_path):
            if os.path.isdir(f"{plugins_path}/{folder}"): 
                plugin_module = importlib.import_module(f"{plugins_pkg}.{folder}")
                for itemName in dir(plugin_module):
                    item = getattr(plugin_module, itemName)
                    try:
                        if issubclass(item, Command):  
                            self.commandHandler.registerCommand(folder, item())
                    except TypeError:
                        continue 
                
        print("Type \"exit\" to exit.")
        while True:
            userInput = input(">>> ").strip()
            userInput = userInput.split() #comma split list
            try:
                command = userInput[0]
                operands = userInput[1:len(userInput)]
                self.commandHandler.executeCommand(command, operands)

            except IndexError: # if no arguments or missing arguments
                print("Arguments were missing: Use 'help' to see proper formating.")
            except TypeError:
                print ("Invalid/Missing arguments: Use 'help' to see proper formatting.")
            except Exception as e:
                print("Unhandled Error: " + str(e))