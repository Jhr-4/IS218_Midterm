from app.commands import Command
import logging
import pandas as pd

#shows most recent 5..
class peekHistoryCommand(Command):
    def execute(self, rows: str=5):
        logging.info(f"peekHistory Command Used.")
        rows = int(rows)
        path = './data/tempHistory.csv'
        df_history = pd.read_csv(path)

        if df_history.empty:
            print('History Is Empty.')
        else:
           print(df_history.tail(rows).to_string())
