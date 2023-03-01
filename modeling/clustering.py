import pandas as pd
import numpy as np
import pickle

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans

#----------------------------------------------------------------------------------

# Import datas
data = pd.read_csv('../data_cleaning/BankChurners.csv')

# Save Attrition columns for Probability estimation
attrition_flag = data['Attrition_Flag']

# Drop unwanted columns
data = data.drop(['Attrition_Flag','CLIENTNUM','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'], axis=1)

# Sort numerical and categorical values
numeric_features = data.select_dtypes(include=['number'])
categorical_features = data.select_dtypes(exclude=['number'])

# Clean datas
data = data.replace({
    'Unknown': np.nan
})

#---------------------------------------------------------

# Pipeline 

# Preprocessing
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler().set_output(transform='pandas'))
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(sparse_output=False).set_output(transform='pandas'))
])

preprocessor = ColumnTransformer(
   transformers=[
    ('numeric', numeric_transformer, numeric_features.columns),
    ('categorical', categorical_transformer, categorical_features.columns)
]).set_output(transform='pandas')

# Model  
pipe_steps = [
    ('preprocessing',preprocessor),
    ('model', KMeans(n_clusters=6, init='random', n_init="auto").set_output(transform='pandas'))]
pipe = Pipeline(pipe_steps)

#---------------------------------------------------------

# Fit the model
cluster_model = pipe.fit(data)

# Save the model as pickle file
filename = './model/test_models/cluster.pkl' 
with open(filename, 'wb') as file:
    pickle.dump(cluster_model, file)
    print("Clustering model saved")

