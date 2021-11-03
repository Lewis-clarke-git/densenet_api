
### Base Image
FROM python:3.9 as base
WORKDIR /code
COPY ./requirements /code/requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements/common.txt

#### Dev Image
FROM base as dev
RUN pip install --no-cache-dir --upgrade -r /code/requirements/dev.txt

#### Production Image
FROM base as production
COPY ./app /code/app
COPY ./model_weights /code/model_weights
RUN pip install --no-cache-dir --upgrade -r /code/requirements/prod.txt
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
