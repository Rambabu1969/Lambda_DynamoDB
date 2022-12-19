from fastapi import FastAPI
from mangum import Mangum

import boto3
dynamodb = boto3.resource('dynamodb')

app = FastAPI()
handler = Mangum(app)

@app.get("/")
async def root():
    return {"greeting":"Hello world"}
    
@app.get("/addStudent")
def addStudent(RollNo: str, Name: str):
    table = dynamodb.Table('mru-students') 
   
    table.put_item(
        Item={
            "RollNo": RollNo,
            "Name": Name
        }
    )   
    return {"message": RollNo + ' saved'}
    
