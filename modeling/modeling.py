import pickle
import numpy as np

path = "modeling/model/classification/classification_model.pkl"

class_model = pickle.load(open(path, "rb"))

def modeling(data : list) -> float:
    features : np.array = [np.array(data)]
    class_prediction : float = class_model.predict(features)
    return class_prediction