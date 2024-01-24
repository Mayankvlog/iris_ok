import unittest
from unittest.mock import patch
import pandas as pd
from main import user_input_features

class TestIrisApp(unittest.TestCase):
    @patch('streamlit.sidebar.slider', side_effect=[5.0, 3.5, 1.4, 0.2])
    def test_user_input_features(self, slider_mock):
        # Simulate a user input feature test
        result = user_input_features()

        expected_result = {
            'Sepal_Length': 5.0,
            'Sepal_Width': 3.5,
            'Petal_Length': 1.4,
            'Petal_Width': 0.2
        }

        self.assertDictEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
#
