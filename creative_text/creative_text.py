import textwrap
import re
import os
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt 
from tqdm import tqdm

class CreativeText:

    def __init__(self):
        self._tags = None
        self._df = None
        self.output_folder_name = "output"
    
    def load_tags(
            self,
            tags
    ):
        """
        Intakes a dictionary of keyword tags and assigns them to the 'self.tags' variable

        Args:
            tags (dictionary):
                - A dictionary of keyword tags

        Returns:
            None

        Note:
            This method updates the 'self.tags' variable with the provided keyword tags dictionary.
        """
        # Check if tag_dict is a dictionary data type
        if not isinstance(tags, dict):
            raise TypeError("'tags' must be a dictionary.")

        # Check if all keys are string and values are list lists of strings
        for key, value in tags.items():
            if not isinstance(key, str):
                raise TypeError(f"Key '{key}' must be a string.")
            if not isinstance(value, list):
                raise TypeError(f"Value for key '{key}' must be a list.")
            if any(not isinstance(item, str) for item in value):
                raise TypeError(f"All items in the list for key '{key}' must be strings.")

        self.tags = tags

    def load_csvs(
            self,
            filepaths,
            skiprows=1
            ):
        """
        Concatenates CSV files into a single pandas DataFrame and assigns it to the 'self.df' varibale.

        Args:
            filepaths (list):
                - List of filepaths for CSV files.

        Returns:
            None

        Note:
            This method updates the 'self.df' variable with concatenated Pandas dataframe of the provided CSV files.
        """

        if not isinstance(filepaths, list):
            raise TypeError("'filepaths' argument must be a list of filepaths.")
        if not filepaths:
            raise ValueError("'filepaths' list cannot be empty.")

        # Initialize an empty list to store DataFrames
        dfs = []

        # Read each CSV file and append its DataFrame to the list
        for filepath in filepaths:
            try:
                df = pd.read_csv(filepath, skiprows=skiprows)
                dfs.append(df)
            except FileNotFoundError as e:
                raise FileNotFoundError(f"The file '{filepath}' was not found. Please double check your spelling and capitalization.")
            except pd.errors.EmptyDataError:
                print(f"Warning: File '{filepath}' is empty. Skipping.")

        if all(df.empty for df in dfs):
            raise pd.errors.EmptyDataError("All inputted csvs are empty.")

        # Concatenate the list of DataFrames into a single DataFrame
        result_df = pd.concat(dfs, ignore_index=True)

        self.df = result_df

    def get_word_frequency(
            self,
            creative_text_column_name="Creative Text",
            ngram_range = (1,2),
            stop_words= "english"
            ):
        """
        Returns a dataframe of word frequency in the 'Creative Text' column of the 'self.df' dataframe.

        Args:
            creative_text_column_name (str):
                - The name of the creative text column in the self.df dataframe.
                - Defaults to "Creative Text"
            ngram_range (tuple):
                - The lower and upper boundary for keyword phrases to search for.
                - For example (1,1), will only search for single word phrases but (1,2) will search for both single word and two word phrases.
                - Defaults to (1,2)
            stop_words (str):
                - Whether or not to remove common stop words from the results. (ex. words like "a", "the", "is", etc.)
                - Defaults to "english"

        Returns:
            Dataframe
                - Returns a pandas dataframe of word frequency in the creative text column of the self.df dataframe.

        Notes:
            - Before running this method, you must first set the 'self.df' variable by using the load_csvs() method.
        """

        # Create a CountVectorizer instance
        vectorizer = CountVectorizer(stop_words=stop_words, ngram_range=ngram_range)

        # Get a list of unique creative text from the self.df dataframe
        creative_text_list = self.df.dropna(subset=[creative_text_column_name])[creative_text_column_name].unique().tolist()

        # Transform the text data into a bag of words representation
        X = vectorizer.fit_transform(creative_text_list)

        # Get the feature names (words)
        feature_names = vectorizer.get_feature_names_out()

        # Convert the result to a dense NumPy array for better visualization
        dense_array = X.toarray()

        # Create a Pandas DataFrame
        df = pd.DataFrame(dense_array, columns=feature_names)

        # If the count of a word is more than 1, then return 1, else return the original number
        # We do this because we don't want the total frequency of each word in the creative text. We only want binary yes or no whether the words was found our not. 
        df = df.map(lambda x: 1 if x > 1 else x)

        # Transform output dataframe
        word_counts = df.sum(axis=0)

        result_df = pd.DataFrame({'word': feature_names, 'frequency_count': word_counts}).reset_index(drop=True)
        result_df["total_unique_creatives_analyzed"] = len(creative_text_list)
        result_df["frequency_percentage"] = round(result_df["frequency_count"] / result_df["total_unique_creatives_analyzed"], 2)

        return result_df.sort_values(by="frequency_count", ascending=False).reset_index(drop=True)

    def tag_creative_text(
            self,
            creative_text,
            tag_name
            ):
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
        if self.tags is None:
            raise RuntimeError("'tags' is not set. Please use the 'set_tags' setter to set desired tags.")
        
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
    
    def get_tagged_creative_text(
            self,
            df,
            creative_text_column_name="Creative Text"
            ):
        """
        Intakes a pandas dataframe and uses the tag_creative_text() method on each row of creative text. 
        For each tag in 'tags' creates a new column with a boolean value for whether tag values were found in the creative text.

        Args:
            df (Dataframe):
                - The pandas dataframe to tag creative text for.
            creative_text_column_name (str):
                - The name of the column that holds ad creative text.
                - Defaults to 'Creative Text'. This is the default creative text column name in Pathmatics Report Builder.

        Returns:
            dataframe:
                - Returns a copy of the inputted dataframe with new columns with boolean values for whether or not tag values were found in the creative text.
        """

        if self.tags is None:
            raise RuntimeError("'tags' is not set. Please use the 'set_tags' setter to set desired tags.")
        
        # There must be a creative text column in the dataframe
        if creative_text_column_name not in df.columns:

            error_message = textwrap.dedent(f"""
                '{creative_text_column_name}' column not found in dataframe.
                Please make sure that you have a creative text column in your dataframe and correctly specify the column name for the 'creative_text_column_name' argument.
                """).strip()
            
            raise ValueError(error_message)

        # Uses the tag_creative_text() method on each creative text row for each tag in the tags dict
        # Creates a new boolean column in the returned df for each tag name
        for tag_name in tqdm(self.tags):
            df[f"{tag_name}"] = df.apply(lambda x: self.tag_creative_text(x[creative_text_column_name], tag_name), axis=1)

        return df  

    def chart_data(
            self,
            df,
            output_file_name,
            spend_column_name="Spend",
            impression_column_name="Impressions"
            ):
        
        if self.tags is None:
            raise RuntimeError("'tags' is not set. Please use the 'set_tags' setter to set desired tags.")

        for metric in [spend_column_name, impression_column_name]:
        
            plt.style.use("seaborn-v0_8")

            # Create number of subplots equal to number of tags
            number_of_subplots = len(self.tags)

            fig, axes = plt.subplots(nrows=number_of_subplots, ncols=1, sharex=True)
            if not isinstance(axes, np.ndarray):
                axes = [axes]

            fig.suptitle(f"Advertising {metric} Over Time By Tag")
            fig.supxlabel("Date")
            fig.supylabel(metric)

            for ax, tag in zip(axes, self.tags):

                filtered_df = df[df[tag] == True].groupby(by=["Date"])[[spend_column_name, impression_column_name]].sum().reset_index()

                ax.plot(pd.to_datetime(filtered_df["Date"]), filtered_df[metric], label=tag)
                ax.legend(loc="upper left")

            plt.gcf().autofmt_xdate()
            plt.tight_layout()

            plt.savefig(f"{self.output_folder_name}/{output_file_name}/{output_file_name}_{metric}_plot.png")
            print(f"{output_file_name}_{metric}_plot.png successfully written to {self.output_folder_name}/{output_file_name} folder")

    def get_tagged_creative_text_csv(
            self,
            file_path_list,
            output_file_name,
            filter_output=True,
            creative_text_column_name="Creative Text",
            spend_column_name="Spend (USD)",
            impressions_column_name="Impressions",
            skiprows=1
            ):

        print("Tagging creative text...")
        
        # Load csvs into an untagged dataframe
        untagged_df = self.load_csvs(file_path_list, skiprows)
        
        # Create new dataframe of tagged creative text
        tagged_df = self.get_tagged_creative_text(untagged_df, creative_text_column_name)
        
        if filter_output is True:
            
            tag_names = list(self.tags.keys())
            
            # Only returns rows where there was a creative text match for at least one of the tag names
            tagged_df = tagged_df[tagged_df[tag_names].any(axis=1)]  

        # If the specified output folder doesn't exist, create a new directory
        if not os.path.isdir(f"{self.output_folder_name}/{output_file_name}"):
            os.makedirs(f"{self.output_folder_name}/{output_file_name}")     
        
        # Write the tagged dataframe to a csv
        tagged_df.to_csv(f"{self.output_folder_name}/{output_file_name}/{output_file_name}.csv", sep=",", encoding="utf-8", index=False)
        print(f"{output_file_name}.csv successfully written to {self.output_folder_name}/{output_file_name} folder")

        self.chart_data(tagged_df, output_file_name, spend_column_name, impressions_column_name)