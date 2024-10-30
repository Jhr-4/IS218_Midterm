import os
from dotenv import load_dotenv

class EnvSettings:

    envlogs = {} #log configuration is dependent on enviornment => hasn't been loaded yet => using dict to store and later display messages
    _settings = {}

    @classmethod
    def load_environment_variables(cls):
        load_dotenv()
        for key, value in os.environ.items():
            cls._settings[key] = value
        cls._settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        cls._settings.setdefault('HISTORY_DIR', './data')

        if (not (cls._settings['HISTORY_DIR'] == './data')):
            cls.check_dir() # checks if the user has put their own history_dir
        cls.envlogs["info"] = [f"Environment variables loaded."]
        print(f"Logging is set to {cls._settings['HISTORY_DIR']}")

    @classmethod
    def check_dir(cls):
        history_dir = cls._settings['HISTORY_DIR']
        if not os.path.exists(history_dir) or not os.access(history_dir, os.W_OK):
            cls.envlogs["error"] = [f"History Directory {history_dir} was does not exit, or is inaccessable."]
            cls._settings['HISTORY_DIR'] = './data' 

    @classmethod
    def get_environment_variable(cls, env_var: str = 'ENVIRONMENT'):
        return cls._settings.get(env_var, None)
    
    @classmethod
    def get_history_dir_variable(cls, env_var: str = 'HISTORY_DIR'):
        return cls._settings.get(env_var, None)