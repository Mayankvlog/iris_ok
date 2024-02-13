import pytest
import streamlit as st
import pandas as pd
from main import user_input_features

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'Sepal_Length': [5.1, 4.9, 4.7],
        'Sepal_Width': [3.5, 3.0, 3.2],
        'Petal_Length': [1.4, 1.4, 1.3],
        'Petal_Width': [0.2, 0.2, 0.2],
        'Species': ['setosa', 'setosa', 'setosa']
    })

def test_user_input_features(sample_data):
    st.sidebar.slider = lambda label, min_value, max_value, value: 5.0
    result = user_input_features()
    
    expected_result = {
        'Sepal_Length': 5.0,
        'Sepal_Width': 5.0,
        'Petal_Length': 5.0,
        'Petal_Width': 5.0
    }

    assert result.to_dict() == expected_result

# Add more test cases for other functionalities
