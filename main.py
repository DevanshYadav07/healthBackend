from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller.diesease import controller as disease_controller


# initialise all the variable
app=FastAPI()

origins =[
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3000/dashboard/diabetes"
    "*"
]

app.include_router(disease_controller,tags=['assistant'])
app.add_middleware(

    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

)