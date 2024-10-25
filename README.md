# IS218 Midterm Calculator Project

This is a Python Calculator CLI application. It allows users to do simple math (add, subtract, multiply, divide) with a working history with pandas that can be cleared, saved, and reloaded.

# Set Up Instructions
- Clone this repository
- Set up an virtual env with dependencies:
  - Install: `pip install virtualenv`
  - Create: `virtualenv -p python3 my_env`
  - Activate: `source my_env/bin/activate`
  - Install Dependencies: `pip3 install -r requirements.txt`
- Run App:
    - `python main.py`

### Setup Developer Environment:
- Create .env file with `ENVIRONMENT=DEVELOPMENT` (Can be changed to PRODUCTION for user view)

# Design Patterns
One important pattern I utilized was adding a "_" to functions that were intended for internal use. This helped create seperation between what should be called and what should be kept only in a file or not by a user. Another important pattern I used was creating a working calculator outside of the application this is important as it allowed for easy troubleshooting. If there was an error with the arithmetic the problem can be isolated and targeted directly into the calculator/operations folder while if there's an error in the actual CLI the focus should be in the app files. Additionally, another design pattern was type hinting in certian functions allowing it to be clear on what type of parameters they take and what they return. This not only helps with the readabilty, but also can help prevent errors of types later on. 

# Analysis of Architectural Decisions
### Logging & Environment Variables:
In this project logging was implemented help in the development process to figure out bugs and keep record of commands that were being utilized. It logs items to the console and into a logs file.

To stop the logging from creating a unfriendly user interface, the environment variable from .env was utilized. By default, it's set to 'PRODUCTION' as regular users wouldn't have this setup. When the environment is set to PRODUCTION the logging does not show up in the console, rather it goes directly to the logs file. This is important as it keeps a clean CLI.

The actual logging process utilized different levels such as INFO, WARNING, and ERROR to easily see the usage of the app. All three of these levels are important to easily see how the application is behaving and functioning. Even for regular users this is important as if they encounter a bug or error they can share this logs file and figure out what's occurring. It can help uncover problems in the application. 

* INFO level outputs are expected and are normal functions or processes of the app like registering plugins. 
* WARNINGS are also similar in that they are normal and occur when there's a minor error that occurs such as an user typing in an invalid argument. 
* ERROR level however, is alittle more serious as when it occurs it indicates errors that were Unhandled or unexpected. 

### LBYL & EAFP
In this project there are many instances of LBYL and EAFP. Both were required as some areas required conditions to be checked while others it was efficient and better to have error handling

* One area where LBYL is utilized is when looking at the commands and arguments the user passes in. This is because the amount of paramters had to be checked. For some commands it required 1 paramater while others required 2. While this could potentially be implemented with EAFP it would be quite inefficient as each command would run expecting an error till the real command runs. This example can be found here [app/commands/\_\_init\_\_.py](https://github.com/Jhr-4/IS218_Midterm/blob/main/app/commands/__init__.py). 

* One area where EAFP was used was in the actual commands. Instead of having tons of if statements that can potentially slow the application down, error handling was utilized to allow the correct command to run and then throw an error message if there was something wrong. For example, instead of having a if statement to check if the command actually exists in a dictionary and then running it could slow down the application if there are too many commands. Therefore, it was more beneficial to just run the command given by the user and have exception handling if the command isn't found. Another example can be seen in the actual running of commands, instead of having multiple if statements to check if the arguments are correct, the command is just ran and gives an exception if something is wrong. These examples can be found here [app/\_\_init\_\_.py](https://github.com/Jhr-4/IS218_Midterm/blob/main/app/__init__.py) & [app/commands/\_\_init\_\_.py](https://github.com/Jhr-4/IS218_Midterm/blob/main/app/commands/__init__.py)
