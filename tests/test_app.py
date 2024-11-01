import pytest
import os
from app import App

def test_AppExit (monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

menuStr = "Commands:\
              \n- menu: This commands menu. \
              \n- exit: Exit the app. \
              \n- add <operand1> <operand2>: Add two numbers.\
              \n- subtract <operand1> <operand2>: Subtract two numbers.\
              \n- multiply <operand1> <operand2>: Multiply two numbers. \
              \n- divide <operand1> <operand2>: Divide two numbers.\
              \n- peekHistory <optional:#>: Get '#' Most Recent Calculations (Default=5).\
              \n- clearHistory: Clear History.\
              \n- saveHistory <name>: Save History to .csv of name <name> in ./data folder. Warning using duplicate names will replace the file.\
              \n- loadHistory <name>: Load History of name <name>.csv. Must be ./data folder and in correct format of operands, operator, and result."

@pytest.mark.parametrize("input, expectedOutput", [
    ("add 50 50", "The result of 50 + 50 is 100"),
    ("subtract 50 100", "The result of 50 - 100 is -50"),
    ("multiply 50 0.5", "The result of 50 * 0.5 is 25"),
    ("divide 50 2", "The result of 50 / 2 is 25"),
    ("divide 50 0", "Division by 0: Undefined"),
    ("add 2 a", f"Invalid Operands: 2 or a is not a valid number."),
    ("wrongCommand 2", f"Invalid Command: wrongCommand, Use 'menu' for commands."),
    ('add', f"Required Arguments Missing"),
    ('', f"Required Arguments Missing"),
    ("menu", menuStr)
])
def test_AppOperationCalculations(input, expectedOutput, capfd, monkeypatch):
    inputs = iter([input, "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert expectedOutput in captured.out.strip()