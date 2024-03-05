import pandas as pd
import pytest
from pathmatics_creative_text.pathmatics_creative_text import PathmaticsCreativeText2

csvs = {
    "valid1": "https://drive.google.com/uc?id=1gQN-5aYhLozZfwAiiPbompKxiE1jPQZY",
    "valid2": "https://drive.google.com/uc?id=15xag1KeOC2MgJb0pJMcwjtpk85l7hgM8",
    "empty1": "https://drive.google.com/uc?id=1LfC9Q0JG9DqhBGAgPbmwG0vFHoaTd3X5",
    "empty2": "https://drive.google.com/uc?id=1q4llyrn0uur8PSjhDjKpLJd_SUiCVvJy"
}

tags = {
    "Console": ["console", "playstation", "xbox"],
    "Mobile": ["mobile", "phone", "smartphone", "android", "ios", "app store"]
}

text_tagger = PathmaticsCreativeText2(tags)

def test_one_valid_csv():

    filepaths = [
        csvs["valid1"]
        ] 
    
    result_dataframe = text_tagger.load_csvs(filepaths)

    assert isinstance(result_dataframe, pd.DataFrame), "Output is not a Pandas DataFrame"

def test_two_valid_csvs():
    
    filepaths = [
        csvs["valid1"],
        csvs["valid2"]
        ] 
    
    result_dataframe = text_tagger.load_csvs(filepaths)

    assert isinstance(result_dataframe, pd.DataFrame), "Output is not a Pandas DataFrame"
 
def test_empty_csvs():

    filepaths = [
        csvs["empty1"],
        csvs["empty2"]
    ]

    with pytest.raises(pd.errors.EmptyDataError):
        text_tagger.load_csvs(filepaths)

def test_invalid_filepaths():

    filepaths = [
        "tests/test_csvs/nonexistantfile1.csv",
        "tests/test_csvs/nonexistantfile2.csv"
    ]

    with pytest.raises(FileNotFoundError):
        text_tagger.load_csvs(filepaths)

def test_empty_filepaths():

    filepaths = []

    with pytest.raises(ValueError):
        text_tagger.load_csvs(filepaths)