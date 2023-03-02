import streamlit as st
import streamlit.components.v1 as components
import time
import pickle

#Personnal function 

from data_preprocessing.fitting_data_model import fitting_data_model_streamlit
from data_preprocessing.preprocessing_users_data import convert_to_numeric_streamlit
from modeling.modeling import modeling 

#Loading the plk file with the dataframe shape the model will need
features_path = "modeling/model/classification/X_form.pkl"
#Loading the pkl file containing a df with the columns used by the ML engineer in his model
df_features = pickle.load(open(features_path, "rb"))

st.set_page_config(page_title="My Dashboard", layout="wide")
with st.container():
    tableau_dashboard = "<div class='tableauPlaceholder' id='viz1677163376923' style='position: relative'><noscript><a href='#'><img alt='Dashboard Analytics ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Cl&#47;ClientProfileDashboard_16771633646050&#47;DashboardAnalytics&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='ClientProfileDashboard_16771633646050&#47;DashboardAnalytics' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Cl&#47;ClientProfileDashboard_16771633646050&#47;DashboardAnalytics&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1677163376923');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1580px';vizElement.style.height='927px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1580px';vizElement.style.height='927px';} else { vizElement.style.width='100%';vizElement.style.height='2577px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"

st.title("Will the customer churn or not ?")

components.html(tableau_dashboard, width=1580, height=927)
with st.sidebar:
    data = dict()

    data['Customer_Age'] = st.number_input('How old is the customer ?', min_value=18, max_value=150)
    #st.write("The customer's age you entered is :", data['Customer_Age'])

    data['Gender'] = st.radio("What's the customer's gender ?", ("Male", "Female"))

    data['Dependent_count'] = st.selectbox("How many dependent relatives do you have ?", ['Select the number please','0','1','2','3','4'])

    data['Marital_Status'] = st.selectbox("What's the customer's marital status ?", ['Select a marital statut please','Divorced','Single','Married','Unknown'])

    data['Education_Level'] = st.selectbox("What's the customer's education's level ?", ["Select the customer's education's level",'Uneducated','College','High School','Graduate','Post-Graduate','Doctorate','Unknown'])

    data['Income_Category'] = st.selectbox("How much does the customer earn a year ?", ['Select an income category please','Less than $40K','Between $40K and $60K','Between $60K and $80K','Between $80K and $120K','Higher than $120K','Unknown'])

    data['Card_Category'] = st.selectbox("What's the customer's card category ?", ['Select a card category please','Blue','Silver','Gold','Platinum'])

    data['Months_on_book'] = st.slider("How long is the customer client in the bank ?", 12, 60, key="months_on_book'")

    data['Total_Relationship_Count'] = st.select_slider("How many products does the customer have in your bank ?", [1,2,3,4,5,6], key="total_relationship_count")

    data['Months_Inactive_12_mon'] = st.select_slider("How many months was the customer inactive during last year ?", [0,1,2,3,4,5,6], key="months_inactive_12_mon")

    data['Contacts_Count_12_mon'] = st.select_slider("How many contacts do you have with the customer last year ?", [0,1,2,3,4,5,6], key="contacts_count_12_mon")

    data['Credit_Limit'] = st.slider("What's the customer's credit's limit ?", 1000, 40000, key="credit_limit")

    data['Total_Revolving_Bal'] = st.number_input("What is the total revolving balance on your credit card ?", min_value=0, max_value=100, key="total_revolving_bal")

    data['Total_Amt_Chng_Q4_Q1'] = st.number_input("How much did the customer's transaction amount change in the last quarter compared to the previous quarter?", min_value=0, max_value=100, key="total_amt_chng_Q4_Q1")

    data['Total_Trans_Amt'] = st.number_input("How much was the customer's total amount transaction for last 12 months ?", min_value=0, max_value=20000, key="total_trans_amt")

    data['Total_Trans_Ct'] = st.number_input("How many transactions did the customer make during last 12 months ?", min_value=0, max_value=200, key="total_trans_ct")

    data['Total_Ct_Chng_Q4_Q1'] = st.number_input("", min_value=0.00, max_value=5.00, key="total_ct_chng_Q4_Q1'")

    data['Avg_Utilization_Ratio'] = st.number_input("What's the ratio for the customer's average card's utilization ?", min_value=0.00, max_value=1.00, key="avg_utilization_ratio")

    #dict for correspondence between values for gender and marital_status column
    correspondence = { "Gender" : {"Male": 0, "Female": 1}, 
                    "Marital_Status" : {"Single": 0, "Married": 1, "Unknown": 2, "Divorced": 3}}
    
    if st.button("Predict") :
        #Convert the data from the form into numerical values
        numeric_data = convert_to_numeric_streamlit(data, correspondence)
        #Preprocessing numeric_data for them to fit the shape the model needs 
        data_fit_model = fitting_data_model_streamlit(numeric_data, df_features)
        predict_churn = modeling(data_fit_model)
        print(df_features)
        print(f"{data_fit_model} has {len(data_fit_model)} length")
        total = 0
        for i, el in enumerate(data_fit_model):
            if el > 0 :
                print(f"the column {i} is fullfilled with the value {el}")
                total += 1
        print(total)
        if predict_churn[0] == 1 :
            st.success("With the data you gave us, it seems the customer will stay in your company !")
            st.balloons()
        else :
            st.error("With the data you gave us, it seems the customer will churn !")
            st.snow()

    #st.write("The button works")
    #st.success("With the data you gave us, it seems the customer will stay in your company !")
    #st.balloons()
    #st.progress(10)
    #with st.spinner('Wait for it...'):    
    #    time.sleep(10)






