import pandas as pd
import re
import os

class PathmaticsCreativeText2:

    def __init__(self, tags):

        # Check if tag_dict is a dictionary data type
        if not isinstance(tags, dict):
            raise TypeError("'tag_dict' must be a dictionary.")
        
        # Check if all keys are string and values are list lists of strings
        for key, value in tags.items():
            if not isinstance(key, str):
                raise TypeError(f"Key '{key}' must be a string.")
            if not isinstance(value, list):
                raise TypeError(f"Value for key '{key}' must be a list.")
            if any(not isinstance(item, str) for item in value):
                raise TypeError(f"All items in the list for key '{key}' must be strings.")
        
        self.tags = tags


    def load_csvs(self, filepaths, skiprows=1):
        """
        Concatenates CSV files into a single pandas DataFrame.

        Args:
            filepaths (list):
                - List of filepaths for CSV files.

        Returns:
            pd.DataFrame: Concatenated DataFrame.
        """

        # Initialize an empty list to store DataFrames
        dfs = []

        # Read each CSV file and append its DataFrame to the list
        for filepath in filepaths:
            try:
                df = pd.read_csv(filepath, skiprows=skiprows)
                dfs.append(df)
            except pd.errors.EmptyDataError:
                print(f"Warning: File '{filepath}' is empty. Skipping.")

        # Concatenate the list of DataFrames into a single DataFrame
        result_df = pd.concat(dfs, ignore_index=True)

        return result_df


#Function(): Load multiple csvs into a single pandas dataframe

#Function(): Intake a creative text string, a the name of th