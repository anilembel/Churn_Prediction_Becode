import pandas as pd

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
from sklearn import set_config




# Import datas
data = pd.read_csv('../2_data cleaning/BankChurners.csv')

# Save Attrition columns for Probability estimation
attrition_flag = data['Attrition_Flag']

# Drop unwanted columns
data = data.drop(['Attrition_Flag','CLIENTNUM','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'], axis=1)

numeric_features =  data.select_dtypes(include=['number'])
categorical_features = data.select_dtypes(exclude=['number'])
# print(categorical.columns)

# Pipeline 
# Preprocessing
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant')),
    ('encoder', OneHotEncoder())
])

preprocessor = ColumnTransformer(
   transformers=[
    ('numeric', numeric_transformer, numeric_features),
    ('categorical', categorical_transformer, categorical_features)
]) 

# Model  
# model = Pipeline(steps=['cluster', KMeans(n_clusters=8, init='random', n_init="auto")] )


pipe_steps = [('pre',preprocessor), ('model', KMeans(n_clusters=8, init='random', n_init="auto"))]
pipe = Pipeline(pipe_steps)


cluster_model = pipe.fit(data)
