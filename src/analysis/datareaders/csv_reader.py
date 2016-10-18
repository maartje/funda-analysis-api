"""CSV reader that loads data from a .csv file into a pandas dataframe."""
import pandas as pd

class CSV_Reader:
    """CSV reader that loads data from a .csv file into a pandas dataframe."""
    
    def __init__(self, filename):
        """Initialize CSV reader."""
        self._filename = filename 

    def get_data(self, columns = None, index_column = None, dtype=None):
        """Return a pandas dataframe containing data from csv file."""
        df = pd.read_csv(self._filename, usecols = columns, index_col = index_column, dtype = dtype)
        return df

# TODO: multiple files + filter duplicates True/False
# remove duplicated records
# df = df[~df.index.duplicated()]
