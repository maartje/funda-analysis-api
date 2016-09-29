import pandas as pd

class CSV_Reader:
    def __init__(self, filename):
        self.filename = filename
        self._data = None

    def get_data(self):
        if self._data == None:
            self._load_data()
        return self._data

    def _load_data(self):
        self._data = None
        # self._data = pd.read_csv(self.filename)