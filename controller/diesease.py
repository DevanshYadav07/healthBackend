from fastapi import APIRouter,FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import json
import pickle
# from chat.suggestion import chatgpt
controller=APIRouter(prefix='/predict')
class Item(BaseModel):
    symptom:str


class Kidney(BaseModel):
    pregnancies:int
    glucose_level:int
    blood_pressure:int
    skin_thickness:int
    bmi:int
    dpf:str
    age:int


class Heart(BaseModel):
    age:int
    sex:int
    cp:int
    trestbps:int
    chol:int
    fbs:int
    restecg:int
    thalach:int
    exang:int
    oldpeak:float
    slope:int
    ca:int
    thal:int


class Diabetes(BaseModel):
    Pregnancies:int
    Glucose:int
    BloodPressure:int
    SkinThickness:int
    Insulin:int
    BMI:float
    DiabetesPedigreeFunction:float
    Age:int



class Liver(BaseModel):
    age:float
    gender:float
    Total_bilirubin:float
    conjucate_bilirubin:float
    Alkaline_phosphate:float
    Alamin_Aminotransferase:float
    Asparated_Aminotransferase:float
    Total_Protiens:float
    Albumin:float
    Alubumin_Globulin_ratio:float


class Parkinson(BaseModel):
    MDVP_fo:float
    MDVP_fi:float
    MDVP_Flo:float
    MDVP_Jitter:float
    MDVP_Jitter_abs:float
    MDVP_RAP:float
    MDVP_PPQ:float
    Jitter_DDP:float
    MDVP_Shimmer:float
    MDVP_Shimmer_dB:float
    Shimmer_APQ3:float
    ShimmerAPQ5:float
    MDVP_APQ:float
    Shimmer_DDA:float
    NHR:float
    HNR:float
    RPDE:float
    DFA:float
    spread1:float
    spread2:float
    D2:float
    PPE:float


# loading the saved models
diabetes_model = pickle.load(open('/Users/devanshyadav/Desktop/Projects/hackky/model/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('/Users/devanshyadav/Desktop/Projects/hackky/model/heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('/Users/devanshyadav/Desktop/Projects/hackky/model/parkinsons_model.sav', 'rb'))



# heart-attack
@controller.post('/heartattack', status_code=200)
def heart_analysist(item:Heart):
    # return {"heart": "you are f*cked"}

    print("symptoms are :",item)
    item_dict = item.dict()

    # Extract values from the dictionary and convert to a list
    item_list = list(item_dict.values())

    print("Symptoms are:", item_list)
    heart_prediction = heart_disease_model.predict(
        [item_list])

    if (heart_prediction[0] == 1):
         return  'The person is having heart disease'
    else:
        return 'The person does not have any heart disease'

    # print('value of heart predi',heart_prediction)

#cancer
@controller.post('/cancer',status_code=200)
def cancer(item:Item):

    print("cancer req body :",item)
    # return{"cancer":'you have in cance '}


#diabetse
@controller.post('/diabetes',status_code=200)
def diabetes(item:Diabetes):

    print("diabetes is  :",item)
    item_dict = item.dict()

    # Extract values from the dictionary and convert to a list
    item_list = list(item_dict.values())
    #
    print("Symptoms are:", item_list)
    heart_prediction = diabetes_model.predict(
        [item_list])

    if (heart_prediction[0] == 1):
        return 'The person is having diabetes disease'
    else:
        return 'The person does not have any diabetes disease'

    # print('value of heart predi',heart_prediction)
    return{"Diabetes":'you have in Diabetes '}


#liver
@controller.post('/liver',status_code=200)
def liver(item:Liver):

    print("we are in liver",item)
    item_dict = item.dict()
    item_list = list(item_dict.values())
    print("liver list: ", item_list,type(item_list))

    model = pickle.load(open('model/liver.pkl','rb'))
    values = np.asarray(item_list)
    print("values array as np;",values,type(values))

    prediction_result = model.predict(values.reshape(1, -1))[0].item()
    # return prediction_result
    if prediction_result==1:
        return 'have liver issue'
    else:
        return 'no liver issue'


#kideny
@controller.post('/kideny',status_code=200)
async def kidney(item:Kidney):

    # print("symptoms are :",item)
    item_dict = item.dict()

    # Extract values from the dictionary and convert to a list
    item_list = list(item_dict.values())

    print("Symptoms are:", item_list)


@controller.post('/parkinson',status_code=200)
async def parkinson(item:Parkinson):

    print("parkinson are :",item)
    item_dict = item.dict()

    # # Extract values from the dictionary and convert to a list
    item_list = list(item_dict.values())
    #
    print("parkinsonSymptoms are:", item_list)
    # return item_list
    parkinsons_prediction = parkinsons_model.predict([item_list])
    #
    if (parkinsons_prediction[0] == 1):
        chat="The person has Parkinson's disease"
        ai_reply= chatgpt(chat)

        # return "The person has Parkinson's disease"
        return { "result":"The person has Parkinson's disease",
                 "suggestion":ai_reply}
    else:
        return {"result": "The person has Parkinson's disease",
        "suggestion": ''}
        # return "The person does not have Parkinson's disease"
