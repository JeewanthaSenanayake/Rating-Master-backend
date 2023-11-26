from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from predict import best_combination, getPrediction
from helper import get_language_code

app = FastAPI()

# Set up CORS
origins = [
    "http://localhost:8080",  # Add the origins (Vue.js app URL) from where requests are allowed
    "http://192.168.43.83:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/get_predict/")
def get_predict(detalis: dict):
    print(detalis['contentName'])
    data ={
            'language': [get_language_code(detalis['language'][0])],
            'titleType': detalis['titleType'],
            'isAdult': detalis['isAdult'],
            'startYear': [float(detalis['startYear'][0])],
            'runtimeMinutes': [float(detalis['runtimeMinutes'][0])],
            'genres': detalis['genres'],
            'director': detalis['director'],
            'writer': detalis['writer'],
            'actor_actress': detalis['actor_actress']
        }
    dataR = getPrediction(data)
    if(dataR):
        time = f"{str(int(float(detalis['runtimeMinutes'][0])/60))}h {str(int(float(detalis['runtimeMinutes'][0])%60))}m"
        return {"rating": {"rating":round(dataR,1), "name":detalis['contentName'], "year":int(detalis['startYear'][0]), "time":time}}
    else:
        raise HTTPException(status_code=500, detail=str('Data error'))


@app.post("/get_best_combination/")
def get_best_combination(detalis:dict):
    data ={
        'language': [get_language_code(x) for x in detalis['language']],
        'titleType': detalis['titleType'],
        'isAdult': detalis['isAdult'],
        'startYear': [float(x) for x in detalis['startYear']],
        'runtimeMinutes': [float(x) for x in detalis['runtimeMinutes']],
        'genres': detalis['genres'],
        'director': detalis['director'],
        'writer': detalis['writer'],
        'actor_actress': detalis['actor_actress']
    }
    dataR = best_combination(data)
    if(dataR):
        return {"data":dataR}
    else:
        raise HTTPException(status_code=500, detail=str('Can not find'))