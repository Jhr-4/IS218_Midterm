import os
import pytest
import pandas as pd
from decimal import Decimal
from calculator import HistoryInput
from calculator import Calculator
from app import App
from app.plugins.peekHistory import peekHistoryCommand
from app.plugins.clearHistory import clearHistoryCommand
from app.plugins.saveHistory import saveHistoryCommand
from app.plugins.loadHistory import loadHistoryCommand
from app.EnvSettings import EnvSettings

class TestHistory:
    @pytest.fixture
    def setup(self):
        self.clearHistory = clearHistoryCommand()
        self.saveHistory = saveHistoryCommand()
        self.loadHistory = loadHistoryCommand()
        self.peekHistory = peekHistoryCommand()


        self.clearHistory.execute()
        HistoryInput._appendHistory(Decimal('10'), Decimal('4'), Calculator._add, Decimal('14'))
        HistoryInput._appendHistory(Decimal('30'), Decimal('.5'), Calculator._subtract, Decimal('29.5'))


    def test_history(self, capfd, setup):
        Calculator.add(Decimal('10'), Decimal('100'))
        self.peekHistory.execute(1) 
        captured = capfd.readouterr()
        assert (
            f'{Decimal("10")}' in captured.out and
            f'{Decimal("100")}' in captured.out and 
            "+" in captured.out and
            f'{Decimal("110")}' in captured.out), "User Calculation into History Broken"
        os.remove(os.path.join(EnvSettings.get_history_dir_variable(),'tempHistory.csv'))
        self.peekHistory.execute()
        captured = capfd.readouterr()
        assert f"No history file of '{os.path.join(EnvSettings.get_history_dir_variable(),'tempHistory.csv')}' found."
        app = App()

    def test_history_clear(self, capfd, setup):
        self.clearHistory.execute()
        self.peekHistory.execute()
        captured = capfd.readouterr()
        assert 'History Is Empty.' in  captured.out, "History Clear Broken"

    def test_history_save(self, capfd, setup):
        self.saveHistory.execute('pytestData')
        rows = pd.read_csv(os.path.join(EnvSettings.get_history_dir_variable(),'pytestData.csv')).shape[0]
        assert rows == 2
        self.clearHistory.execute()
        self.saveHistory.execute('pytestData')
        captured = capfd.readouterr()
        assert 'History Is Empty, Nothing to Save.' in captured.out, "Save Empty History Has Problem"

    def test_history_load(self, caplog, setup):
        self.loadHistory.execute('pytestData')
        rows = pd.read_csv(os.path.join(EnvSettings.get_history_dir_variable(),'tempHistory.csv')).shape[0]
        assert rows == 4
        os.remove(os.path.join(EnvSettings.get_history_dir_variable(),'pytestData.csv'))
        self.loadHistory.execute('pytestData')
        assert f"{os.path.join(EnvSettings.get_history_dir_variable(), 'pytestData.csv')} not found." in  caplog.text, "Load History Has Problem"