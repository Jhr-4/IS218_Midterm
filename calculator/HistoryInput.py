import logging
import os
import pandas as pd
from decimal import Decimal
from typing import Callable
from app.EnvSettings import EnvSettings 

class HistoryInput:


    data_csv = 'tempHistory.csv'

    @classmethod
    def _setup_History(cls):
        data_dir = EnvSettings.get_history_dir_variable()

        if data_dir == './data': 
            #This is just another safety check 
            #If not ./data -> the dir should already exit w/ acceess (made sure when loading the env variables) 
            try:
                os.makedirs(data_dir)
                logging.info(f"The directory '{data_dir}' is created")
            except FileExistsError:
                logging.debug(f"The directory '{data_dir}' already existed.")
                if not os.access(data_dir, os.W_OK):
                    logging.error(f"The directory '{data_dir}' is not writable.")
                    return
        
        data = {
            'Operand_1:': [],
            'Operand_2:': [],
            'Operator:': [],
            'Result:': []
            }

        df_history = pd.DataFrame(data)
        csv_file_path = os.path.join(data_dir, cls.data_csv)
        df_history.to_csv(csv_file_path, index=False)
        

        logging.info(f"Created a empty CSV at '{csv_file_path}'.")


    @classmethod
    def _appendHistory(cls, a: Decimal, b: Decimal, operation: Callable[[Decimal,Decimal],Decimal], result: Decimal):
        data_dir = EnvSettings.get_history_dir_variable()
        operations = {
            '_add': '+',
            '_subtract': '-',
            '_divide': '/',
            '_multiply': '*'
        }
        
        input = {
            'Operand_1': [a],
            'Operand_2': [b],
            'Operator': [operations[operation.__name__]], 
            'Result': [result]
            }

        df_input = pd.DataFrame(input)
        csv_file_path = os.path.join(data_dir, 'tempHistory.csv')
        df_input.to_csv(csv_file_path, mode='a', header=False, index=False)
