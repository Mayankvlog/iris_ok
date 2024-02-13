import pytest
import streamlit as st
from main import user_input_features

def test_user_input_features():
    # Simulate a user input feature test
    sepal_length = 5.0
    sepal_width = 3.5
    petal_length = 1.4
    petal_width = 0.2

    # Simulate user input within the expected range
    with pytest.raises(st.ScriptRunner.StopException):
        with pytest.raises(SystemExit):
            with unittest.mock.patch('streamlit.sidebar.slider', side_effect=[sepal_length, sepal_width, petal_length, petal_width]):
                result = user_input_features()

    expected_result = {
        'Sepal_Length': sepal_length,
        'Sepal_Width': sepal_width,
        'Petal_Length': petal_length,
        'Petal_Width': petal_width
    }

    assert result == expected_result

# Add more test cases for other functionalities
