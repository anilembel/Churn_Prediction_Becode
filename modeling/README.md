# Project Overview  

Based on customers bank profile, build a model to predict the possibility for a customer to churn or not,
using a classification model.
Run a clustering model to determine different customer profile and the propability to churn for each profile.

## 1.Classification

The classification model used for this project is KNN from SKlearn
Model is build in classification.py.  
Model is saved in a pickle file in model/classification
### Preprocessing

Starting from the raw datas, removing non relevant columns.
Selection of the features and target (Existing or Attrited Customer) for the model.
Splitting the datas to train and test samples
Data analysis reveils the dataset is imbalanced.  
Using RandomOverSampler, train set is balanced to 50%.  

![Alt text](Pictures/classification/imbalanced.png)  

![Alt text](Pictures/classification/RandomOverSampler.png)

### Feature selection  

Based on PCA analysis during clustering, the most important features are selected for the two models (until gender).

![Alt text](Pictures/feature_importance_clustering.png)

## Pipeline  

Building a model pipeline:

- SimpleImputer to fill some missing values

- For numeric datas: StandardScaler for scaling the values.
- For categorical datas: OneHotEncoder -> categorical to numerical datas

![Alt text](Pictures/classification/model_classification.png)

- Model :

GridSearch and cross validation on the main parameter of the model(n_neighbors)
Best result used is n_neighbors = 9 with an accuracy of 87.53 %.  

![Alt text](Pictures/classification/gridsearch.png)

### Confusion Matrix  

The classification model is trained to detect chrurning customer profiles.
The worst case scenario would be to detect an attrited customer as an existing customer (False Negative).  
False negative are 218 or 2,15% , as shown in the confusion matrix.
The scoring metric minimizing the False Negative is recall = (TP/TP+FN).
The recall returns the proportion of positive values correctly predicted.  
Result for the classification model:  
Accuracy: 92%
Recall: 87%

![Alt text](Pictures/classification/Confusion%20Matrix%20Classification.png)

<img src="Pictures/classification/classification_report.png" width="500" height="auto" />

### Improvements  

- Select another model  
- test random scaler down  
- hyper parameters optimisation  

## 2.Clustering  

The classification model used for this project is KMeans.
Model is build in clustering.py.  
Model is saved in a pickle file in model/clustering

## Pipeline

![Alt text](Pictures/clustering/pipelineClustering.png)

Determine the number of clusters in the customers profiles.

Based on elbow graph and silhouette score, the most relevant number of clusters is between 6 and 7.  
6 Clusters gives the best results.  
Cluster 3 has a greater probability of churning.

![Alt text](Pictures/clustering/elbow.png)  

The probability of churning is determined for each clusters.  

![Alt text](Pictures/clustering/clusters_propabilities.png)  

![Alt text](Pictures/clustering/probaGrapgh.png)  

![Alt text](Pictures/clustering/clusters3D.png)  
