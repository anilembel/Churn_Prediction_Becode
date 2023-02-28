import pickle 

#I'd like to just change that path  and everything else would be automated !!!
features_path = "modeling/models/X_form.pkl"

#Loading the pkl file containing a df with the columns used by the ML engineer in his model
df_features = pickle.load(open(features_path, "rb"))

#Creating a dict with each column's name associated to his column's nb
def dict_column_name_position(df_features) -> dict:
    column_position : dict = dict()
    for nb,column in enumerate(df_features.columns):
        column_position[column] = nb
    return column_position

def list_n_elements (n : int, value : any) -> list:

    """Creating a list of n values attribuating each element the value defined
    with the type you need"""

    created_list = [value for x in range(n)]

    return created_list


def fitting_data_model_flask(data : dict, df_features) -> list:
    #Taking the nb of columns who is the nb of features
    nb_features = df_features.shape[1]
    # Create a list with n elements n = nb of features of the model (X_train)
    # assigning each element the value 0
    fitting_data : list = list_n_elements(nb_features, 0)
    column_position : dict = dict_column_name_position(df_features)
    #print(f"Column position = {column_position}")
    #print(f"Data = {data}")
    for column_name_reference, position in column_position.items():
        for column_name_stored, value in data.items():
            if column_name_reference == column_name_stored :
                fitting_data[position] = int(value)
            elif "Education" in column_name_stored :
                if "College" in value :
                    fitting_data[column_position['Education_Level_College']] = 1
                elif "Doctorate" in value :
                    fitting_data[column_position['Education_Level_Doctorate']] = 1
                elif "Post-Graduate" in value :
                    fitting_data[column_position['Education_Level_Post-Graduate']] = 1
                elif "Graduate" in value :
                    fitting_data[column_position['Education_Level_Graduate']] = 1
                elif "High School" in value :
                    fitting_data[column_position['Education_Level_High School']] = 1
                elif "Uneducated" in value :
                    fitting_data[column_position['Education_Level_Uneducated']] = 1
                elif "Unknown" in value :
                    fitting_data[column_position['Education_Level_Unknown']] = 1
            elif "Income" in column_name_stored:
                if "than $120K" in value:
                    fitting_data[column_position['Income_Category_$120K +']] = 1
                elif "$40K and $60K" in value:
                    fitting_data[column_position['Income_Category_$40K - $60K']] = 1
                elif "$60K and $80K" in value :
                    fitting_data[column_position['Income_Category_$60K - $80K']] = 1
                elif "$80K and $120K" in value :
                    fitting_data[column_position['Income_Category_$80K - $120K']] = 1
                elif "than $40K" in value :
                    fitting_data[column_position['Income_Category_Less than $40K']] = 1
                elif "Unknown" in value :
                    fitting_data[column_position['Income_Category_Unknown']] = 1
            elif "Card" in column_name_stored:
                if "Blue" in value:
                    fitting_data[column_position['Card_Category_Blue']] = 1
                elif "Gold" in value:
                    fitting_data[column_position['Card_Category_Gold']] = 1
                elif "Platinum" in value :
                    fitting_data[column_position['Card_Category_Platinum']] = 1
                elif "Silver" in value:
                    fitting_data[column_position['Card_Category_Silver']] = 1
    for k in data.keys():
        for column_name in column_position.keys():
            print(f"{k} = {column_name}")
    return fitting_data



def fitting_data_model_streamlit(data : dict, df_features) -> list:
    #Taking the nb of columns who is the nb of features
    nb_features = df_features.shape[1]
    fitting_data : list = list_n_elements(nb_features,0)
    column_position : dict = dict_column_name_position(df_features)
    
    for column_name_reference, position in column_position.items():
        for column_name_stored, value in data.items():
            if column_name_reference == column_name_stored :
                fitting_data[position] = int(value)
            elif "Education" in column_name_stored :
                if "College" in value :
                    fitting_data[column_position['Education_Level_College']] = 1
                elif "Doctorate" in value :
                    fitting_data[column_position['Education_Level_Doctorate']] = 1
                elif "Post-Graduate" in value :
                    fitting_data[column_position['Education_Level_Post-Graduate']] = 1
                elif "Graduate" in value :
                    fitting_data[column_position['Education_Level_Graduate']] = 1
                elif "High School" in value :
                    fitting_data[column_position['Education_Level_High School']] = 1
                elif "Uneducated" in value :
                    fitting_data[column_position['Education_Level_Uneducated']] = 1
                elif "Unknown" in value :
                    fitting_data[column_position['Education_Level_Unknown']] = 1
            elif "Income" in column_name_stored:
                if "than $120K" in value:
                    fitting_data[column_position['Income_Category_$120K +']] = 1
                elif "$40K and $60K" in value:
                    fitting_data[column_position['Income_Category_$40K - $60K']] = 1
                elif "$60K and $80K" in value :
                    fitting_data[column_position['Income_Category_$60K - $80K']] = 1
                elif "$80K and $120K" in value :
                    fitting_data[column_position['Income_Category_$80K - $120K']] = 1
                elif "than $40K" in value :
                    fitting_data[column_position['Income_Category_Less than $40K']] = 1
                elif "Unknown" in value :
                    fitting_data[column_position['Income_Category_Unknown']] = 1
            elif "Card" in column_name_stored:
                if "Blue" in value:
                    fitting_data[column_position['Card_Category_Blue']] = 1
                elif "Gold" in value:
                    fitting_data[column_position['Card_Category_Gold']] = 1
                elif "Platinum" in value :
                    fitting_data[column_position['Card_Category_Platinum']] = 1
                elif "Silver" in value:
                    fitting_data[column_position['Card_Category_Silver']] = 1
    return fitting_data        

