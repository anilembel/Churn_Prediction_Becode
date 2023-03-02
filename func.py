import streamlit as st

#Function who create and collect the data on streamlit app
def collecting_data(df):
    gender = st.radio("What's the customer's gender ?", ("Male", "Female"))
    if gender == "Male":
        df.loc['Gender'] = 'M'
    else :
        df.loc['Gender'] = 'F'

    df['Customer_Age'] = st.slider('How old is the customer ?',18 ,100, key="Customer_Age")

    df['Dependent_count'] = st.slider("How many dependent relatives does the customer have ?", 0, 6, key="Dependent_count")

    df['Months_on_book'] = st.slider("How long is the customer client in your bank ? (in months)", 13, 60, key="months_on_book'")

    df['Total_Relationship_Count'] = st.slider("How many products does the customer have in your bank ?", 0, 6, key="total_relationship_count")

    df['Months_Inactive_12_mon'] = st.slider("How many months was the customer inactive during last year ? (months)", 0, 6, key="months_inactive_12_mon")

    df['Contacts_Count_12_mon'] = st.slider("How many contacts do you have with the customer last year ?", 0, 6, key="contacts_count_12_mon")

    df['Credit_Limit'] = st.slider("What's the customer's credit's limit ? ($)", 1400, 40000, key="credit_limit")

    df['Total_Revolving_Bal'] = st.slider("What is the total revolving balance on the customer's credit card ? ($)", 0, 3000, key="total_revolving_bal")

    df['Total_Amt_Chng_Q4_Q1'] = st.slider("How much did the customer's transaction amount change in the last quarter compared to the previous quarter?", 0, 5, key="total_amt_chng_Q4_Q1")

    df['Total_Trans_Amt'] = st.slider("How much was the customer's total amount transaction for last 12 months ? ($)", 0, 20000, key="total_trans_amt")

    df['Total_Trans_Ct'] = st.slider("How many transactions did the customer make during last 12 months ?", 0, 200, key="total_trans_ct")

    df['Total_Ct_Chng_Q4_Q1'] = st.slider("How much did the customer's transaction amount changed in the last quarter compared to the previous one ?", 0.00, 5.00, key="total_ct_chng_Q4_Q1'")

    df['Avg_Utilization_Ratio'] = st.slider("What's the ratio for the customer's average card's utilization ?", 0.00, 1.00, key="avg_utilization_ratio")

    return df