from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controller.diesease import controller as disease_controller


# initialise all the variable
app=FastAPI()

origins =[
    "*"
]


@app.get('/')
def test():
    return {"hello" : "route is working fine "}



app.include_router(disease_controller,tags=['assistant'])
app.add_middleware(

    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)