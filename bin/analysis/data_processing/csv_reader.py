"""CSV reader that lazily loads Funda data from a .csv file into a pandas dataframe."""
import pandas as pd

class CSV_Reader:
    """CSV reader that lazily loads Funda data from a .csv file into a pandas dataframe."""
    
    def __init__(self, filename, columns = None, index_column = None):
        """Initialize CSV reader."""
        self.filename = filename
        self.columns = columns
        self.index_column = index_column
        self._data = None

    def get_data(self):
        """Return a pandas dataframe containing Funda data."""
        if self._data == None:
            self._load_data()
        return self._data

    def _load_data(self):
        self._data = pd.read_csv(self.filename, usecols = self.columns, index_col = self.index_column) 
