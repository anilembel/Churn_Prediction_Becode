import pickle
import numpy as np


class_model = pickle.load(open("modeling/models/classification_model.pkl", "rb"))

def modeling(data : list) -> float:
    features : np.array = [np.array(data)]
    class_prediction : float = class_model.predict(features)
    return class_prediction