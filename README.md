# IS218 Midterm Calculator Project

This is a Python Calculator CLI application. It allows users to do simple math (add, subtract, multiply, divide) with a working history with pandas that can be cleared, saved, and reloaded.

# [Video Demonstration](https://www.youtube.com/watch?v=WA_Qok1SIU0)

# Set Up Instructions

### Setup App/Project
- Clone this repository
- Set up an virtual env with dependencies:
  - Install: `pip install virtualenv`
  - Create: `virtualenv -p python3 my_env`
  - Activate: `source my_env/bin/activate`
  - Install Dependencies: `pip3 install -r requirements.txt`
- Run App:
    - `python main.py`

### Setup Environment Variables:
- Create .env file 
- To change to developer mode add this line `ENVIRONMENT=DEVELOPMENT` (Can be changed to PRODUCTION for user view)
- To change the history save path use `HISTORY_DIR='/DIRECT/PATH'` (This directory path has the be already created).

### Pytest
- To test the code with the written tests utilize `pytest` and to check coverage use `pytest --cov` 

# Usage
After running the application with `python main.py`, the list of commands can be obtained by typing `menu`. This will give all the functionality of the app.

To summarize the application can perform addition, subtraction, multiplication, and division of 2 digit numbers (decimal & integers).
  * The command looks general command `<operation> <operand1> <operand2>`

Furthermore, a functional history was added to save the commands to a .csv file when using the app. 
  * The history can be accessed in the application via `peekHistory` and cleared with `clearHistory`. 
  * The history .csv can be saved with `saveHistory <name>` and reloaded using `loadHistory <name>`.

# Design Patterns
One important design pattern used was [Single Responsibility](https://www.cleancode.studio/design-patterns/single-responsibility-design-pattern), which ensures modularity. For example, everything is separate from the calculator, history, to the actual app. Each one of these things has smaller functions like [add and subtract](https://github.com/Jhr-4/IS218_Midterm/blob/main/calculator/__init__.py) that does one specific task. This allows errors to be found easily and also it to be easily read. 

Another design pattern used was the [Facade design pattern](https://www.geeksforgeeks.org/facade-design-pattern-introduction/) which was utilized in the CLI. Users only have access to certain commands from the plugins and can't use or see anything that is occurring behind the scene. This is a facade as it masks and hides all the complexity behind the scenes.  

Additionally, a similar pattern to Singleton is utilized as the [EnvSettings](https://github.com/Jhr-4/IS218_Midterm/blob/main/app/EnvSettings.py) only gets created once and is referred to by a get function afterwards across multiple files. However, it's not fully singleton as the code doesn't ensure only one instance is created. 

# Analysis of Architectural Decisions
### Logging & Environment Variable:
In this project logging was implemented help in the development process to figure out bugs and keep record of commands that were being utilized. It logs items to the console and into a logs file.

To stop the logging from creating a unfriendly user interface, the environment variable from .env was utilized. By default, it's set to 'PRODUCTION' as regular users wouldn't have this file setup. When the environment is set to PRODUCTION the regular logging does not show up in the console, rather it goes directly to the logs file. It only shows the error and higher logs in console as this is important feedback for the user. It is important to not show all the logs to keep a clean CLI. 

The actual logging process utilized different levels such as DEBUG, INFO, WARNING, and ERROR to easily see the usage of the app. All three of these levels are important to easily see how the application is behaving and functioning. Even for regular users this is important as if they encounter a bug or error they can share this logs file and figure out what's occurring. It can help uncover problems in the application. 

* DEBUG level was utilized (only visible to those in developer environment) to log messages when testing the app.
* INFO level were used as outputs that are expected and are normal functions or processes of the app like registering plugins. 
* WARNINGS are also similar in that they are normal and occur when there's a minor error that occurs such as an user typing in an invalid argument. 
* ERROR level however, is alittle more serious as it indicates errors that were due to something like a file not found or an unhandled/unexpected error. 

#### [More Information on Logging](https://docs.python.org/3/howto/logging.html)

### History and DIR Variable:
* To make the history work pandas was utilized which creates a .csv and saves the operations the user runs. There is also functionality to save the history and load a saved history. To allow users to save the files outside of the program the environment variable HISTORY_DIR was used to allow users to specify where they want the history to go instead of directly occurring in the program.  
  * To see the code on how .env variables were loaded: [app/EnvSettings.py](https://github.com/Jhr-4/IS218_Midterm/blob/main/app/EnvSettings.py)

### LBYL & EAFP
In this project there are many instances of LBYL and EAFP. Both were required as some areas required conditions to be checked while others it was efficient and better to have error handling

* One area where LBYL is utilized is when looking at the commands and arguments the user passes in. This is because the amount of parameters had to be checked. For some commands it required 1 pparameter while others required 2. While this could potentially be implemented with EAFP it would be quite inefficient as each command would run expecting an error till the real command runs. This example can be found here [app/commands/\_\_init\_\_.py](https://github.com/Jhr-4/IS218_Midterm/blob/main/app/commands/__init__.py). Furthermore, in the history files to check if a file exists and is writable it made sense to use if statements to check the conditions rather than directly using a try catch.

* One area where EAFP was used was in the actual commands. Instead of having tons of if statements that can potentially slow the application down, error handling was utilized to allow the correct command to run and then throw an error message if there was something wrong. For example, instead of having a if statement to check if the command actually exists in a dictionary and then running it could slow down the application if there are too many commands. Therefore, it was more beneficial to just run the command given by the user and have exception handling if the command isn't found. Another example can be seen in the actual running of commands, instead of having multiple if statements to check if the arguments are correct, the command is just ran and gives an exception if something is wrong. These examples can be found here [app/\_\_init\_\_.py](https://github.com/Jhr-4/IS218_Midterm/blob/main/app/__init__.py) & [app/commands/\_\_init\_\_.py](https://github.com/Jhr-4/IS218_Midterm/blob/main/app/commands/__init__.py)

#### [More Information on LBYL vs. EAFP](https://realpython.com/python-lbyl-vs-eafp/)