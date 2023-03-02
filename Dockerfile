#Importing the base's image to create our own Docker image
FROM python:3.10

#Defining the work directory for the docker's container
WORKDIR /app

#Copying requirements.txt into Docker image
COPY requirements_deployment.txt .

#Launch the pip upgrading
RUN python -m pip install --upgrade pip

#Installing the requirements
RUN pip install -r requirements_deployment.txt

#Copy the needed folder from local to Docker's image
COPY . .

#Defining the port 8501 as the port Docker must use for Streamlit  
EXPOSE 8501

#Launch the python file app_streamlit_normal.py
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

#docker build -t churn_predict_app .   #Creating docker image (the name must be without Uppercase)
#docker run -t -i -p 8501:8501 churn_predict_app #Creating the docker container

#pipreqs --savepath requirements_streamlit.txt .churn