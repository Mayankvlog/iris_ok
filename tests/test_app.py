import pytest
import streamlit as st
from main import user_input_features

def test_user_input_features():
    # Simulate a user input feature test
    sepal_length = 5.0
    sepal_width = 3.5
    petal_length = 1.4
    petal_width = 0.2

    # Mock Streamlit elements
    mock_slider = st._components['st.slider']

    with mock_slider('Sepal Length', 4.3, 7.9, 5.4), \
         mock_slider('Sepal Width', 2.0, 4.4, 3.4), \
         mock_slider('Petal Length', 1.0, 6.9, 1.3), \
         mock_slider('Petal Width', 0.1, 2.5, 0.2):

        result = user_input_features()

    expected_result = {
        'Sepal_Length': sepal_length,
        'Sepal_Width': sepal_width,
        'Petal_Length': petal_length,
        'Petal_Width': petal_width
    }

    assert result == expected_result

# Add more test cases for other functionalities
