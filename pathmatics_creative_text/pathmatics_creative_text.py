import pandas as pd
import re
import os
from tqdm import tqdm

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


    def tag_creative_text(self, creative_text, tag_name):
        """
        Intakes a string of creative text and looks for presence of keywords specified in the 'self.tags' dictionary.

        Args:
            creative_text (str):
                - Creative text string to analyze.
            tag_name (str):
                - Tag name to use when matching creative text.

        Returns:
            bool:
                - True if any tag values are found in the given creative text
                - Else, False
        """

        if tag_name not in self.tags:
            raise KeyError(f"tag_name '{tag_name}' not found in 'tags' dictionary.")

        creative_text = str(creative_text)

        # Tag values to search creative_text for
        tag_values = self.tags[tag_name]

        # Loop through each tag value and see if tag is present in creative text
        matches = []
        for tag_value in tag_values:

            # Only matches if target word is between two spaces
            search_object = re.search(r"\b" + tag_value + r"\b", creative_text, flags=re.I)
            matches.append(search_object)

        # If any of the tag values are found in the creative_text, return True, else return False
        return any(matches)
    

    def get_tagged_creative_text(self, df, creative_text_column_name="Creative Text"):

        # There must be a creative text column in the dataframe
        if creative_text_column_name not in df.columns:
            raise Exception(f"No '{creative_text_column_name}' column not found in dataframe. Please make sure that you have a creative text column in your dataframe and correctly specify the column name for the 'creative_text_columns_name' argument")

        # Uses the tag_creative_text() method on each creative text row for each tag in the tags dict
        # Creates a new boolean column in the returned df for each tag name
        for tag_name in tqdm(self.tags):
            df[f"{tag_name}"] = df.apply(lambda x: self.tag_creative_text(x[creative_text_column_name], tag_name), axis=1)

        return df  