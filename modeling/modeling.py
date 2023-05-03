import pickle

path = "modeling/model/classification/classification_model.pkl"

class_model = pickle.load(open(path, "rb"))

def modeling(df):
    class_prediction = class_model.predict(df)
    return class_prediction