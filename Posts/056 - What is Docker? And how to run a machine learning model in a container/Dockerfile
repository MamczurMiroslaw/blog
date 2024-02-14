# choose python version
FROM python:3.9.10

# Set up a working directory
WORKDIR /code

# copy python requirements
COPY app/requirements.txt /code/requirements.txt

# update pip
RUN pip install --no-cache-dir --upgrade pip

# install requirements
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copy our FastApi application
COPY ./app /code/app

# run app
CMD ["uvicorn", "app.step5-rebuild:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
