import unittest
import pandas as pd

class TestDataQuality(unittest.TestCase):
    """
    A class to test the data quality of a pandas DataFrame.
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

    def test_missing_values(self):
        """
        Test for missing values in the DataFrame.
        """
        # Check if there are any missing values in 'column1'
        self.assertTrue(self.data['column1'].isnull().any(), "Column1 should have missing values.")
        
        # Ensure there are no missing values in 'column2' and 'column3'
        self.assertFalse(self.data['column2'].isnull().any(), "Column2 should not have missing values.")
        self.assertFalse(self.data['column3'].isnull().any(), "Column3 should not have missing values.")

    def test_column_data_types(self):
        """
        Test for correct data types in the DataFrame.
        """
        # Check that 'column1' is of numeric type
        self.assertTrue(pd.api.types.is_numeric_dtype(self.data['column1']), "Column1 should be numeric.")
        
        # Check that 'column3' is of string type
        self.assertTrue(pd.api.types.is_string_dtype(self.data['column3']), "Column3 should be a string.")

if __name__ == '__main__':
    unittest.main()
