from app.commands import Command
import logging
import pandas as pd
from app.EnvSettings import EnvSettings

class clearHistoryCommand(Command):
    def execute(self):
        logging.info(f"clearHistory Command Used.")

        path = f'{EnvSettings.get_history_dir_variable()}/tempHistory.csv'
        df_history = pd.read_csv(path)

        df_emptyHistory = df_history.drop(df_history.index)
        df_emptyHistory.to_csv(path, index=False)