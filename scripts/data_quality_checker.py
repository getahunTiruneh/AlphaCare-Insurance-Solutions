import pandas as pd
import numpy as np

class DataQualityChecker:
    """
    A class to perform data quality checks on a pandas DataFrame.
    """
    def __init__(self, data):
        """
        Initialize with a pandas DataFrame.
        """
        self.data = data
    def check_missing_values(self):
        """
        Check for missing values in the DataFrame.

        Returns:
            dict: A dictionary where keys are column names and values are booleans indicating
            whether the column contains missing values.
        """
        return {col: self.data[col].isnull().any() for col in self.data.columns}
    def check_data_types(self, expected_types):
        """
        Check if the columns in the DataFrame have the expected data types.
        Args:
            expected_types (dict): A dictionary with column names as keys and expected data types as values.
        Returns:
            dict: A dictionary where keys are column names and values are booleans indicating whether
            the column matches the expected data type.
        """
        return {col: pd.api.types.is_dtype_equal(self.data[col].dtype, dtype) 
                for col, dtype in expected_types.items()}

    def check_duplicates(self):
        """
        Check for duplicate rows in the DataFrame.
        Returns:
            bool: True if there are duplicate rows, False otherwise.
        """
        return self.data.duplicated().any()

    def run_all_checks(self, expected_types):
        """
        Run all data quality checks and return a summary.
        Args:
            expected_types (dict): A dictionary of expected data types for columns.
        Returns:
            dict: A dictionary summarizing the results of all data quality checks.
        """
        return {
            "missing_values": self.check_missing_values(),
            "data_types": self.check_data_types(expected_types),
            "duplicates": self.check_duplicates(),
        }
