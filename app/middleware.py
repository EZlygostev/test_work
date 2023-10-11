from fastapi import FastAPI
from pydantic import BaseModel
from db import DBPostgres

class Body(BaseModel):
    questions_num: int

class RecordsResponse():
    def __init__(self):
        self.list_response = ['']
        
    def set_record(self, value):
        self.list_response.append(value)

app =  FastAPI()
db_postgre = DBPostgres()
