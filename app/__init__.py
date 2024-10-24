import os
import importlib
from app.commands import CommandHandler
from app.commands import Command
import logging
import logging.config

class App:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        self.commandHandler = CommandHandler()

    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def enable_plugins(self):
        plugins_pkg = 'app.plugins'
        plugins_path = 'app/plugins'
        
        if plugins_path is None:
            logging.error("Plugins Directory Not Found: " + plugins_path)
            return

        for pluginFolder in os.listdir(plugins_path):
            if os.path.isdir(os.path.join(plugins_path, pluginFolder)):
                #TRY import
                try:
                    plugin_module = importlib.import_module(f"{plugins_pkg}.{pluginFolder}")
                    for itemName in dir(plugin_module):
                        item = getattr(plugin_module, itemName)
                        #TRY REGISTER
                        try: 
                            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                                self.commandHandler.registerCommand(pluginFolder, item())
                                logging.info("Registered " + pluginFolder + " From " + itemName + " Plugin.")
                        except TypeError:
                            continue
                except ImportError as e:
                    logging.error(f"Error Importing Plugin {pluginFolder}: {e}")

    def start(self):
        self.enable_plugins()
        logging.info("Application started.")
        print("Type \"exit\" to exit.")
        while True:
            userInput = input(">>> ").strip()
            userInput = userInput.split() #comma split list
            try:
                command = userInput[0]
                operands = userInput[1:len(userInput)]
                self.commandHandler.executeCommand(command, operands)

            except IndexError: # if no arguments or missing arguments --> happens when just one argument missing or no command
                logging.warning("Command or Required Arguments Missing.")
                print("Command or Required Arguments Missing: Use 'menu' to see proper formating.")
            except TypeError: # happens when just typing operation
                logging.warning("Required Arguments were Missing.")
                print ("Required Arguments Missing: Use 'menu' to see proper formatting.")
            except Exception as e: # just incase
                logging.error("Unhandled Error: " + str(e))
                print("Unhandled Error: " + str(e))