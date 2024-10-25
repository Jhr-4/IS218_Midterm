from app.commands import Command
import logging
import pandas as pd

class clearHistoryCommand(Command):
    def execute(self):
        logging.info(f"clearHistory Command Used.")

        path = './data/tempHistory.csv'
        df_history = pd.read_csv(path)

        df_emptyHistory = df_history.drop(df_history.index)
        df_emptyHistory.to_csv(path, index=False)