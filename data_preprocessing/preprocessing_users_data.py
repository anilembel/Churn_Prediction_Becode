from flask import request

def convert_request_form_into_dict_flask() -> dict:
    if request.method == 'POST':
        #Defining the dict who will store the form's info
        received_data = dict()
        for k,v in request.form.items():
            received_data[k] = v
    return received_data

def convert_to_numeric_streamlit (data_to_convert : dict, correspondence : dict) -> dict:
    """This function will convert the data collected by the web form into numerical data for the model to predict a result
    It takes the dict data_to_convert where the data from the form are stored and the dict correspondence with the correspondence
    to convert the non numerical values from the first into numerical values with the second. With this method, if needed, I could 
    add features into the form and in the correspondence dict for this function to automatically convert them as weel"""

    for k, v in data_to_convert.items() :
        for dictionnary in correspondence :
            if k == dictionnary :
                #print(f"The key {k} is eqal to dict {dictionnary}")
                for key, value in correspondence[dictionnary].items():
                    if data_to_convert[k] == key :
                        data_to_convert[k] = value
                        #print(f"I just assigned : {data_to_convert[k]} = {value}")
                              
    return data_to_convert