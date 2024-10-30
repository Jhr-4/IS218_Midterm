import os
from app.commands import Command
import logging
import pandas as pd
from app.EnvSettings import EnvSettings

#shows most recent 5..
class saveHistoryCommand(Command):
    def execute(self, name: str):

        name = name+".csv"
        data_dir = EnvSettings.get_history_dir_variable()
        data_csv = 'tempHistory.csv'

        try:
            df_history = pd.read_csv(os.path.join(data_dir, data_csv))

            if df_history.empty:
                print('History Is Empty, Nothing to Save.')
            else:
                csv_file_path = os.path.join(data_dir, os.path.join(name))
                df_history.to_csv(csv_file_path, index=False)
            

                logging.info(f"Created a copy CSV at '{csv_file_path}'.")
                
        except FileNotFoundError:
            logging.error(f"{os.path.join(data_dir, data_csv)} not found.")
            print("The default temporary history file is missing.")
