import sys
from app.commands import Command
import logging

class ExitCommand(Command):
    def execute(self):
        logging.info("Exited with exit command.")
        sys.exit("Exiting Calculator Application...")