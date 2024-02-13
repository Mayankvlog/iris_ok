import pytest
import pandas as pd
import streamlit as st
from main import user_input_features

def test_user_input_features():
    st.sidebar.slider = lambda label, min_value, max_value, value: {
        'Sepal Length': 5.0,
        'Sepal Width': 3.5,
        'Petal Length': 1.4,
        'Petal Width': 0.2
    }[label]
    
    result = user_input_features()
    expected_result = pd.DataFrame({
        'Sepal Length': [5.0],
        'Sepal Width': [3.5],
        'Petal Length': [1.4],
        'Petal Width': [0.2]
    })
    
    pd.testing.assert_frame_equal(result, expected_result)
