import os
import sys
import importlib
from dotenv import load_dotenv
from app.commands import CommandHandler
from app.commands import Command
from app.EnvSettings import EnvSettings
import logging
import logging.config
from calculator.HistoryInput import HistoryInput

class App:
    def __init__(self):
        os.makedirs('logs', exist_ok=True)
        EnvSettings.load_environment_variables()
        self.environment = EnvSettings.get_environment_variable()
        self.history_dir = EnvSettings.get_history_dir_variable()
        self.configure_logging()
        for level in EnvSettings.envlogs:
            for messages in EnvSettings.envlogs[level]:
                #for message in messages:
                if level == 'warning':
                    logging.warning(messages)
                if level == 'error':
                    logging.error(messages)

        self.commandHandler = CommandHandler()
        HistoryInput._setup_History()


    def configure_logging(self):
        #Dynamic logging configuration through environment variables
        if self.environment=='DEVELOPMENT':
            logging_conf_path = 'logging_configs/logging_dev.conf'
        else: 
            logging_conf_path = 'logging_configs/logging_prod.conf'

        try:
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        except FileNotFoundError:
            logging.warning("Logging config file not found. Set to basicConfig.")
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
        logging.info("-----Application Started-----")
        self.enable_plugins()
        print("Type \"exit\" to exit.")
        while True:
            try:
                userInput = input(">>> ").strip()
                userInput = userInput.split() #comma split list
                command = userInput[0]
                args = userInput[1:len(userInput)]
                self.commandHandler.executeCommand(command, args)

            except IndexError: # if no arguments or missing arguments --> happens when just one argument missing or no command
                logging.warning("Command or Required Arguments Missing.")
                print("Command or Required Arguments Missing: Use 'menu' to see proper formating.")
            except TypeError: # happens when just typing operation
                logging.warning("Required Arguments were Missing.")
                print ("Required Arguments Missing: Use 'menu' to see proper formatting.")
            except KeyboardInterrupt:
                logging.info("Application interrupted and exiting gracefully.")
                sys.exit("Exiting Calculator Application...")
            except ValueError:
                logging.warning(f"Invalid Args Used: {args}")
                print(f"Invalid Arguments. Use 'menu' to see proper formatting.")
            except Exception as e: # just incase
                logging.error("Unhandled Error: " + str(e))
                print("Unhandled Error: " + str(e))