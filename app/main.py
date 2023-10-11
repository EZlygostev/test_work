import requests, json
from settings import url_test
from middleware import app, Body
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from middleware import db_postgre, RecordsResponse

@app.post('/')
def get_test_api(body: Body):
    rec_response = RecordsResponse()
    for itter in range(body.questions_num):
        while True:
            response = requests.get(url=url_test)
            if response.status_code!=200:
                raise HTTPException(status_code=500, detail="Failed request")
            else:
                response = response.json()[0]
                request_data = (
                        response['id'],
                        response['answer'],
                        response['question'],
                        response['created_at']
                    )
                if db_postgre.set_record(request_data):
                    rec_response.set_record(response['answer'])
                    break
    return JSONResponse([
                            {
                                "before_answer" : rec_response.list_response[-2],
                                "all_answer": rec_response.list_response[1:]
                             }
                            ])

