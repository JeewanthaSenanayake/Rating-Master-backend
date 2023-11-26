import joblib
import pandas as pd

from helper import adultNot, get_language_name

model = joblib.load('models\imdb_LR_model_v2.joblib')

# X_new = pd.DataFrame({
#     'language': ['en'],
#     'titleType': ['short'],
#     'isAdult': [0],
#     'startYear': [1895],
#     'runtimeMinutes': [1],
#     'genres': ['documentary'],
#     'director': ['louis lumière'],
#     'writer': ['other'],
#     'actor_actress': ['other']
# })

# ratings = model.predict(X_new)

# print(ratings)

def best_combination(details:dict):
    combinationList =[]
    try:
        for language in details['language']:
            for titleType in details['titleType']:
                for isAdult in details['isAdult']:
                    for startYear in details['startYear']:
                        for runtimeMinutes in details['runtimeMinutes']:
                            for genres in details['genres']:
                                for director in details['director']:
                                    for writer in details['writer']:
                                        for actor_actress in details['actor_actress']:
                                            X_inpt = pd.DataFrame(
                                                {
                                                    'language': [language],
                                                    'titleType': [titleType],
                                                    'isAdult': [isAdult],
                                                    'startYear': [startYear],
                                                    'runtimeMinutes': [runtimeMinutes],
                                                    'genres': [genres],
                                                    'director': [director],
                                                    'writer': [writer],
                                                    'actor_actress': [actor_actress]
                                                })
                                            ratings = model.predict(X_inpt)
                                            newRatings = {
                                                    'language': get_language_name(language),
                                                    'titleType': titleType,
                                                    'isAdult': adultNot(isAdult),
                                                    'startYear': startYear,
                                                    'runtimeMinutes': runtimeMinutes,
                                                    'genres': genres,
                                                    'director': director,
                                                    'writer': writer,
                                                    'actor_actress': actor_actress,
                                                    "rating":round(list(ratings)[0],1)
                                                }
                                            combinationList.append(newRatings)
        
        return sorted(combinationList, key=lambda x: x['rating'], reverse=True)[:5]
    except:
        return False

def getPrediction(detalis:dict):
    
    try:

        X_new = pd.DataFrame(detalis)
        ratings = model.predict(X_new)
        return list(ratings)[0]
    
    except:
        return False
    

#pip install dill
