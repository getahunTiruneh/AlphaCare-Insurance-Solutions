import unittest
import pandas as pd
from scripts.data_quality_checker import DataQualityChecker

class TestDataQuality(unittest.TestCase):
    """
    A class to test the data quality of a pandas DataFrame using DataQualityChecker.
    """

    def setUp(self):
        """
        Set up the test data.
        """
        self.data = pd.DataFrame({
            'column1': [1, 2, 3, None],
            'column2': [4, 5, 6, 7],
            'column3': ['a', 'b', 'c', 'd']
        })
        self.data_quality_checker = DataQualityChecker(self.data)

    def test_missing_values(self):
        """
        Test for missing values in the DataFrame.
        """
        missing_values = self.data_quality_checker.check_missing_values()
        self.assertTrue(missing_values['column1'], "Column1 should have missing values.")
        self.assertFalse(missing_values['column2'], "Column2 should not have missing values.")
        self.assertFalse(missing_values['column3'], "Column3 should not have missing values.")

    def test_data_types(self):
        """
        Test for correct data types in the DataFrame.
        """
        expected_types = {
            'column1': 'float64',
            'column2': 'int64',
            'column3': 'object'  # Strings in pandas are of object type
        }
        data_types = self.data_quality_checker.check_data_types(expected_types)
        self.assertTrue(data_types['column1'], "Column1 should be of type float.")
        self.assertTrue(data_types['column2'], "Column2 should be of type int.")
        self.assertTrue(data_types['column3'], "Column3 should be of type object.")

    def test_duplicates(self):
        """
        Test for duplicate rows in the DataFrame.
        """
        self.assertFalse(self.data_quality_checker.check_duplicates(), "There should be no duplicate rows.")

if __name__ == '__main__':
    unittest.main()
