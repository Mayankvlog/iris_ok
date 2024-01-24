import unittest
import streamlit as st
from main import user_input_features

class TestIrisApp(unittest.TestCase):
    def test_user_input_features(self):
        # Simulate a user input feature test
        sepal_length = 5.0
        sepal_width = 3.5
        petal_length = 1.4
        petal_width = 0.2

        with self.subTest(msg="Slider within expected range"):
            # Simulate user input within the expected range
            with unittest.mock.patch('streamlit.sidebar.slider', return_value=sepal_length), \
                 unittest.mock.patch('streamlit.sidebar.slider', return_value=sepal_width), \
                 unittest.mock.patch('streamlit.sidebar.slider', return_value=petal_length), \
                 unittest.mock.patch('streamlit.sidebar.slider', return_value=petal_width):
                result = user_input_features()

            expected_result = {
                'Sepal_Length': sepal_length,
                'Sepal_Width': sepal_width,
                'Petal_Length': petal_length,
                'Petal_Width': petal_width
            }

            self.assertEqual(result, expected_result)

    # Add more test cases for other functionalities

if __name__ == '__main__':
    unittest.main()
