""" Filter for removing rows with missing values. """

import math

class FilterMissingValues:
    """ Filter for removing rows with missing values. """

    def __init__(self, required_fields = []):
        """Initialize FilterMissingValues."""
        self._required_fields = required_fields

    def process(self, df):
        """ Return the dataframe without the rows that miss values for required fields."""
        df = df[df.apply(self._filter_records_missing_data, axis = 1)]
        return df
        
    def _filter_records_missing_data(self, row):
        for column_name in self._required_fields:
            if self._is_missing(row[column_name]):
                return False
        return True
    
    def _is_missing(self, value):
        return isinstance(value, float) and math.isnan(value)
    
