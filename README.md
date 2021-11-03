# DenseNetAPI
DenseNetAPI implements a DenseNet121 model with trained weights behind an API. This allows users to submit images to the API and the model will return predictions as a string.

# Project layout
    .
    ├── app                 # Application Files 
    │   ├── model           # DenseNet121 and preprocessing
    │   ├── routers         # API routes
    │   ├── main.py         # main.py for the Application
    │   ├── schemas.py      # schemas.py for the API messages
    ├── model_weights       # Weights to be loaded into the DenseNet121 
    ├── requirements        # Requirements for the Development and Production stages 
    ├── test                # Automated tests 
    ├── docker-compose.yml  # For launching the stages locally
    ├── dockerfile          # For creating the docker image    
    └── README.md

# Setup Instructions
To run DenseNetAPI you will need to have docker installed.
The development environment can be started by running:

`docker-compose up dev`

Or the production environment can be started by running:

`docker-compose up prod`

Once this is completed the API should be available from `localhost:5000` for development or `localhost:8080` for production.
Documentation can be found at `localhost:5000/docs`.

# How it works 
This project has two environment, development and production. The production environment does not contain the testing framework or the test code.

Once one of the environments is up, images can be sent to the model using the API by posting to `localhost:5000/predict`. The image must be in the json format {"image": "IMAGE_DATA"}. The model will then return the json response {"response": "PREDICTION"}. This can be tested using the `localhost:5000/docs` or by using curl.

# Automated Testing
While running the development environment automated tests can be ran in the docker container.
First access the docker container using:

`docker exec -it densenetapi_dev /bin/bash`

Once in the docker container just run pytest with the command below:

`pytest`
