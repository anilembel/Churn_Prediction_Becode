<h2 align="center"> Churn prediction project </h2>
<p align="center"><a href="https://github.com/anilembel/Churn_Prediction_Becode">
<img src=".streamlit/BeCode_color.png" alt="Logo"></a></p>
<h3 align="center">First project in our AI specialization at <a href="https://github.com/becodeorg"><strong>BeCode</strong></a></h3><br><br>

## Description

This repository host our first group project in our chosen specialization.

We worked on given data in order to predict whether or not a bank client is likely to churn. In order to do so, we analyzed the data to define different clusters, we then trained a model to make the prediction and finally, we deployed an easy to use app which let our users know if a specific client is at risk of churning.

The project is divided in 5 folders:

1. data_storage: upload the given .csv file to a database.
2. data_cleaning: contains graphs and cleaned data for data analyst and ML engineer.
3. data_preprocessing: preprocessing of the data for the ML engineer.
4. modeling: classification, clustering and modeling used for the prediction.
5. vizualisations: creation of client profile dashboard with Tableau.

## Installation

1. Clone the repo.
2. Install the required libraries using

   ```
   pip install requirments.txt
   ```

   * imbalanced_learn 0.10.1
   * imblearn 0.0
   * matplotlib.pyplot 3.7.0
   * numpy 1.24.2
   * pandas 1.5.3
   * pillow 9.4.0
   * plotly.graph_objects
   * plotly.subplots
   * scikit-learn 1.2.1
   * seaborn 0.12.2
   * skimpy
   * sqlite3 5.1.2
   * streamlit 1.19.0
3. Launch our app using

   ```
   streamlit run "app.py"
   ```

## Usage

app.py

#### data_storage

As required, we uploaded the .csv file into a database.
We used sqlite as it was sufficient for the (non) usage we made of it afterward.

#### data_cleaning

[work in progress]

#### modeling

[work in progress]

#### vizualisations

[work in progress]

## Results

[work in progress]

## Contact

data analyst: [Anil Furkan EMBEL ](https://github.com/anilembel)
ML engineer: [Philippe Meulemans](https://github.com/Laverdure77)
data engineers: [Romain Vanden Bossche](https://github.com/vdbromain) & [Anh Sophie Noël](https://github.com/AnhSN)
