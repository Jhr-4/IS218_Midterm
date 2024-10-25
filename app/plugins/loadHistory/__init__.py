import os
from app.commands import Command
import logging
import pandas as pd

class loadHistoryCommand(Command):
    def execute(self, name: str):

        name = name+".csv"
        data_dir = './data'
        data_csv = 'tempHistory.csv'

        try:
            df_curr_history = pd.read_csv(os.path.join(data_dir, data_csv))
        except FileNotFoundError:
            logging.error(f"{os.path.join(data_dir, data_csv)} not found.")
            print("The default temporary history file is missing.")
        try:
            df_load_history = pd.read_csv(os.path.join(data_dir, name))
        except FileNotFoundError:
            logging.error(f"{os.path.join(data_dir, name)} not found.")
            print(f"No history file named {name} found.")

        try:
            df_curr_history.dropna(axis=1, how='all', inplace=True)
            df_load_history.dropna(axis=1, how='all', inplace=True)

            df_combined = pd.concat([df_curr_history, df_load_history], ignore_index=True)
            df_combined.to_csv(os.path.join(data_dir, data_csv), index=False)
        except Exception as e:
            logging.error(f"Unhandled Error: {e}")
            print(e)