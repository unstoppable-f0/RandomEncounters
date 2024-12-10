from pathlib import Path
from os import environ, path
from sys import exit

from dotenv import load_dotenv


class DBSettings:
    def __init__(self):
        self.user_name = environ.get('USER_NAME')
        self.password = environ.get('PASSWORD')
        self.host = environ.get('HOST')
        self.port = environ.get('PORT')
        self.database = environ.get('DB_NAME')

    @property
    def dsn(self) -> str:
        return f'postgresql+psycopg://{self.user_name}:{self.password}@{self.host}:{self.port}/{self.database}'


main_dir_path = Path(__file__).parent.parent
dotenv_path = path.join(main_dir_path, '.env')
if path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    print('No .env file found. Please add it and try again.')
    exit()
