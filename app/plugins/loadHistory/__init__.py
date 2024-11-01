import os
from app.commands import Command
import logging
import pandas as pd
from app.EnvSettings import EnvSettings

class loadHistoryCommand(Command):
    def execute(self, name: str):

        user_csv = name+".csv"
        logging.info(f"loadHistory on Command Used on {user_csv}")
        data_dir = EnvSettings.get_history_dir_variable()
        temp_data_csv = 'tempHistory.csv'

        #read current temp file
        try:
            df_curr_history = pd.read_csv(os.path.join(data_dir, temp_data_csv))
        except FileNotFoundError:
            logging.error(f"The default temporary history file '{os.path.join(data_dir, temp_data_csv)}' not found.")
            return

        #read user history file
        try:
            df_load_history = pd.read_csv(os.path.join(data_dir, user_csv))
        except FileNotFoundError:
            logging.error(f"{os.path.join(data_dir, user_csv)} not found.")
            return

        try:
            df_curr_history.dropna(axis=1, how='all', inplace=True)
            df_load_history.dropna(axis=1, how='all', inplace=True)

            df_combined = pd.concat([df_curr_history, df_load_history], ignore_index=True)
            df_combined.to_csv(os.path.join(data_dir, temp_data_csv), index=False)
        except Exception as e:
            logging.error(f"Unhandled Error: {e}")