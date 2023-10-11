import dotenv, os

#load environment from .env
dotenv.load_dotenv()

#url for connect test API
url_test = 'https://jservice.io/api/random?count=1'

#DB connect
DB_NAME = os.getenv('DB_NAME')
DB_PASSWORD = os.getenv('DB_PASSWORT')
DB_USER = os.getenv('DB_USER')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

#DB field
TABLE_NAME = 'test_question'
ID_RECORD = 'id'
ID_QUESTION = 'id_question'
ANSWER = 'answer'
QUESTION = 'question'
CREATED = 'created'