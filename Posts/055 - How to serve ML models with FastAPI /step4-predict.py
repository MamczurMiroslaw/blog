from fastapi import FastAPI
from sklearn.datasets import load_iris
from pydantic import BaseModel

import pickle

# Creating FastAPI instance
app = FastAPI()
iris = load_iris()


# Creating class to define the request body and the type hints of each attribute
class request_body(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


# Creating an Endpoint to receive the data to make prediction on.
@app.post('/predict')
def predict(data: request_body):
    # Making the data in a form suitable for prediction
    test_data = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    # Load the saved model from file
    model_filename = "./model/random_forest_model.pkl"
    with open(model_filename, 'rb') as model_file:
        loaded_model = pickle.load(model_file)

    # Predicting the Class
    class_idx = loaded_model.predict(test_data)[0]

    # Return the Result
    return {'class_index': str(class_idx),
            'class_name': iris.target_names[class_idx]}
