#Importing the base's image to create our own Docker image
FROM python:3.10

#Defining the work directory for the docker's container
WORKDIR /app

#Copying requirements.txt into Docker image
#COPY requirements.txt .
COPY requirements_streamlit.txt .
#Launch the pip upgrading
RUN python -m pip install --upgrade pip

#Installing the requirements
#RUN pip install -r requirements.txt
RUN pip install -r requirements_streamlit.txt


#Copy the needed folder from local to Docker's image
COPY . .

#Defining the port 4999 as the port Docker must use
#For streamlit is port : 8501
#EXPOSE 4999   
EXPOSE 8501
#Launch the python file app.py
#For streamlit : ENTRYPOINT ["streamlit", "run", "app_streamlite.py", "--server.port=8501", "--server.address=0.0.0.0"]
#CMD ["python", "app_Flask.py"]
ENTRYPOINT ["streamlit", "run", "app_streamlit_normal.py", "--server.port=8501", "--server.address=0.0.0.0"]

#docker build -t churn_predict_app .   #Creating docker image (the name must be without Uppercase)
#docker run -t -i -p 4999:4999 churn_predict_app #Creating the docker container

#pipreqs --savepath requirements_streamlit.txt .churn