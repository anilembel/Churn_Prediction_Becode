import pandas as pd
import numpy as np
import pickle

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

from imblearn.over_sampling import RandomOverSampler

#----------------------------------------------------------------------------------
# Import datas
data = pd.read_csv('../data_cleaning/BankChurners.csv')

# Select columns
select= ['Attrition_Flag','Gender', 'Customer_Age', 'Dependent_count', 
        'Months_on_book', 'Total_Relationship_Count', 
        'Months_Inactive_12_mon', 'Contacts_Count_12_mon', 
        'Credit_Limit', 'Total_Revolving_Bal', 'Total_Amt_Chng_Q4_Q1', 
        'Total_Trans_Amt', 'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1', 
        'Avg_Utilization_Ratio'
        ]

data = pd.concat([data[select]], axis=1)

# Clean datas
data = data.replace({
    'Unknown': np.nan
})

#--------------------------------------------------------
# Select target and features

# Select features
features = data.drop(['Attrition_Flag'], axis=1)

# Select target
target = data['Attrition_Flag']

#---------------------------------------------------------
# Select features for prediction test
attrited_clients = data.loc[data['Attrition_Flag'] == 'Attrited Customer'].drop(['Attrition_Flag'], axis=1).iloc[:5]

#---------------------------------------------------------
# Check for imbalanced target
print(f"Check for imbalanced target: \n{target.value_counts(normalize=True) * 100}")

#---------------------------------------------------------
# Split Test/Train 
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=38)

#---------------------------------------------------------
# Select numerical and categorical features
numeric_features = features.select_dtypes(include=['number']).columns.to_list()
categorical_features = features.select_dtypes(exclude=['number']).columns.to_list()

#---------------------------------------------------------
# Over sampling on train to train the model with more balanced datas(50%)
ros = RandomOverSampler(random_state=0, sampling_strategy=.5)
X_train, y_train = ros.fit_resample(X_train, y_train)

#---------------------------------------------------------
# Check for imbalanced target
print(f"Balanced train datas: \n{y_train.value_counts(normalize=True) * 100}")

#---------------------------------------------------------
# Pipeline 
optimal_kn = 9

# Preprocessing steps
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler().set_output(transform='pandas'))
])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(sparse_output=False).set_output(transform='pandas'))
])

# Column transformer
preprocessor = ColumnTransformer(
   transformers=[
    ('numeric', numeric_transformer, numeric_features),
    ('categorical', categorical_transformer, categorical_features)
]).set_output(transform='pandas')

# Model steps
pipe_steps = [
    ('preprocessing',preprocessor),
    ('model', KNeighborsClassifier(n_neighbors=optimal_kn))]

# Build Pipe
pipe = Pipeline(pipe_steps)

#---------------------------------------------------------
# Fit the model
classification_model = pipe.fit(X_train, y_train)

# Score
accuracy_test = round(pipe.score(X_test, y_test),3)   # model predict on X_test, and compare pred to y_test
print(accuracy_test)

# Test Prediction
for i in range(0,5):
    result = pipe.predict(attrited_clients.iloc[[i]])[0]
    if result == 'Attrited Customer':
        flag = '👍'
    else: 
        flag = '👎'
    print(f"Prediction: {result}, Should be Attrited Customer {flag}.")


#---------------------------------------------------------
# Save the model as pickle file
filename = './model/classification/classification_model.pkl' 
with open(filename, 'wb') as file:
    pickle.dump(classification_model, file)
    print("Clustering model saved")

# Empty features df for predictions, stored in model folder
X_form = pd.DataFrame(columns=features.columns)
X_form.to_pickle('./model/classification/X_form.pkl')
