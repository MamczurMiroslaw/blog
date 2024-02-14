# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import pickle


def train_model(test_size=0.50):
    # Load the Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=2023)

    # Initialize the Random Forest classifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

    # Train the model
    rf_classifier.fit(X_train, y_train)

    # Predict on the test set
    y_pred = rf_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # Save the trained model to a file using pickle
    model_filename = "app/model/random_forest_model.pkl"
    with open(model_filename, 'wb') as model_file:
        pickle.dump(rf_classifier, model_file)

    return rf_classifier, accuracy


model, accuracy = train_model()
print(f'{round(100*accuracy,2)}%')
