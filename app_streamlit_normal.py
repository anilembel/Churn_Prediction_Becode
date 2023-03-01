import streamlit as st
#To add the link of the dashboard with the embeded code from Tableau
import streamlit.components.v1 as components
#To load the model
import pickle
#To import the image (favicon)
from PIL import Image

import pandas as pd

#Personnal function 

from data_preprocessing.fitting_data_model import fitting_data_model_streamlit
from data_preprocessing.preprocessing_users_data import convert_to_numeric_streamlit
from modeling.modeling import modeling 

#Loading the plk file with the dataframe shape the model will need
features_path = "modeling/model/classification/X_form.pkl"
#Loading the pkl file containing a df with the columns used by the ML engineer in his model
df = pickle.load(open(features_path, "rb"))

#Open the favicon image
img = Image.open(".streamlit/save-money.png")
#To take the page on the whole width for the dashboard to be displayed on its entirety
st.set_page_config(page_title="Churn Prediction", layout="wide", page_icon=img)

#Put a title as it'd be with <h1> in html
st.title("Welcome to our app to predict if your customer will churn or not !")
st.write("You can juste fill in the form before and click on the button 'Predict' to know if the customer could churn or not.")
st.write("""Just keep in mind, with the data we received, your customer has to be already a client for 13 months at least to be able to give
        you a prediction on the churn.""")

#Radio button Female / Male beside each other
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
gender = st.radio("What's the customer's gender ?", ("Male", "Female"))
if gender == "Male":
    df.loc['Gender'] = 'M'
else :
    df.loc['Gender'] = 'F'

df['Customer_Age'] = st.slider('How old is the customer ?',18 ,100, key="Customer_Age")

df['Dependent_count'] = st.slider("How many dependent relatives does the customer have ?", 0, 6, key="Dependent_count")

#data['Marital_Status'] = st.selectbox("What's the customer's marital status ?", ['Select a marital statut please','Divorced','Single','Married','Unknown'])

#data['Education_Level'] = st.selectbox("What's the customer's education's level ?", ["Select the customer's education's level",'Uneducated','College','High School','Graduate','Post-Graduate','Doctorate','Unknown'])

#data['Income_Category'] = st.selectbox("How much does the customer earn a year ?", ['Select an income category please','Less than $40K','Between $40K and $60K','Between $60K and $80K','Between $80K and $120K','Higher than $120K','Unknown'])

#data['Card_Category'] = st.selectbox("What's the customer's card category ?", ['Select a card category please','Blue','Silver','Gold','Platinum'])

df['Months_on_book'] = st.slider("How long is the customer client in your bank ? (in months)", 13, 60, key="months_on_book'")

df['Total_Relationship_Count'] = st.slider("How many products does the customer have in your bank ?", 0, 6, key="total_relationship_count")

#data['Months_Inactive_12_mon'] = st.select_slider("How many months was the customer inactive during last year ?", [0,1,2,3,4,5,6], key="months_inactive_12_mon")
df['Months_Inactive_12_mon'] = st.slider("How many months was the customer inactive during last year ? (months)", 0, 6, key="months_inactive_12_mon")

df['Contacts_Count_12_mon'] = st.slider("How many contacts do you have with the customer last year ?", 0, 6, key="contacts_count_12_mon")

df['Credit_Limit'] = st.slider("What's the customer's credit's limit ? ($)", 1400, 40000, key="credit_limit")

df['Total_Revolving_Bal'] = st.slider("What is the total revolving balance on the customer's credit card ? ($)", 0, 3000, key="total_revolving_bal")

df['Total_Amt_Chng_Q4_Q1'] = st.slider("How much did the customer's transaction amount change in the last quarter compared to the previous quarter?", 0, 5, key="total_amt_chng_Q4_Q1")

df['Total_Trans_Amt'] = st.slider("How much was the customer's total amount transaction for last 12 months ? ($)", 0, 20000, key="total_trans_amt")

df['Total_Trans_Ct'] = st.slider("How many transactions did the customer make during last 12 months ?", 0, 200, key="total_trans_ct")

df['Total_Ct_Chng_Q4_Q1'] = st.slider("How much did the customer's transaction amount changed in the last quarter compared to the previous one ?", 0.00, 5.00, key="total_ct_chng_Q4_Q1'")

df['Avg_Utilization_Ratio'] = st.slider("What's the ratio for the customer's average card's utilization ?", 0.00, 1.00, key="avg_utilization_ratio")

#dict for correspondence between values for gender and marital_status column
#correspondence = { "Gender" : {"Male": "M", "Female": "F"}}#, 
#                "Marital_Status" : {"Single": 0, "Married": 1, "Unknown": 2, "Divorced": 3}}

print(df)

#st.write('<style>.stButton>button{display:block;margin:0 auto;}</style>', unsafe_allow_html=True)
st.write('<style>.stButton>button{display:block;margin:0 auto;font-size:24px;width:200px;height:80px;}</style>', unsafe_allow_html=True)

if st.button("Predict") :

    #Convert the data from the form into numerical values
    #numeric_data = convert_to_numeric_streamlit(data, correspondence)
    #Preprocessing numeric_data for them to fit the shape the model needs 
    #data_fit_model = fitting_data_model_streamlit(numeric_data, df_features)
    #Predicting the churn with the classification model
    predict_churn = modeling(df)
    if predict_churn[0] == "Attrited Customer":
        st.write('<style>.stButton>button{display:block;margin:0 auto;}</style>', unsafe_allow_html=True)
        st.write("With the data you gave us, it seems the customer should churn your bank !")
        st.snow()

    else :
        st.write('<style>.stButton>button{display:block;margin:0 auto;}</style>', unsafe_allow_html=True)
        st.write("With the data you gave us, it seems the customer should stay in your bank !")
        st.balloons()


#To make 2 lines of space between the button and the dashboard
st.write("")
st.write("")
st.header("Here is the dashboard :")
#Old_version tableau_dashboard = "<div class='tableauPlaceholder' id='viz1677163376923' style='position: relative'><noscript><a href='#'><img alt='Dashboard Analytics ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Cl&#47;ClientProfileDashboard_16771633646050&#47;DashboardAnalytics&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='ClientProfileDashboard_16771633646050&#47;DashboardAnalytics' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Cl&#47;ClientProfileDashboard_16771633646050&#47;DashboardAnalytics&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1677163376923');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1580px';vizElement.style.height='927px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1580px';vizElement.style.height='927px';} else { vizElement.style.width='100%';vizElement.style.height='2577px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
st.write("Dashboard explanations")
tableau_dashboard = "<div class='tableauPlaceholder' id='viz1677667958870' style='position: relative'><noscript><a href='#'><img alt='Dashboard Analytics ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;GY&#47;GYZ6GWSPJ&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='path' value='shared&#47;GYZ6GWSPJ' /> <param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;GY&#47;GYZ6GWSPJ&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1677667958870');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1580px';vizElement.style.height='927px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1580px';vizElement.style.height='927px';} else { vizElement.style.width='100%';vizElement.style.height='2677px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
components.html(tableau_dashboard, width=1580, height=927)

#st.write("The button works")
#st.success("With the data you gave us, it seems the customer will stay in your company !")
#st.balloons()
#st.progress(10)
#with st.spinner('Wait for it...'):    
#    time.sleep(10)






