import pytest
import streamlit as st
import pandas as pd
from main import user_input_features, make_prediction  # Import necessary functions

def test_user_input_features():
    # Use Pytest to test the user_input_features function

    # Simulate user input
    with pytest.raises(Exception):  # Use Pytest to capture Streamlit exceptions
        with st.sidebar:
            st.sidebar.slider('Sepal Length', 4.3, 7.9, 5.4)
            st.sidebar.slider('Sepal Width', 2.0, 4.4, 3.4)
            st.sidebar.slider('Petal Length', 1.0, 6.9, 1.3)
            st.sidebar.slider('Petal Width', 0.1, 2.5, 0.2)

    # Assuming the user_input_features returns a DataFrame
    features = user_input_features()

    # You can add assertions based on the expected behavior of your function
    assert isinstance(features, pd.DataFrame)
    assert features.shape == (1, 4)

    # Add more assertions based on the behavior of your function

def test_prediction():
    # Use Pytest to test the prediction functionality

    # Load the Iris dataset
    data = pd.read_csv('data/iris.csv')  # Adjust the path accordingly

    # Simulate user input
    user_input = {
        'Sepal_Length': 5.0,
        'Sepal_Width': 3.0,
        'Petal_Length': 1.0,
        'Petal_Width': 0.2
    }

    # Assuming you have a function for making predictions
    prediction = make_prediction(user_input, data)  # Adjust the function name accordingly

    # You can add assertions based on the expected behavior of the prediction
    assert isinstance(prediction, str)  # Assuming the prediction is a string

