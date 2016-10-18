""" Filter for removing rows with missing values. """

import math

class FilterMissingValues:

    def __init__(self, required_fields = []):
        self.required_fields = required_fields

    def process(self, df):
        """ Return a dataframe with cleaned Funda data.
        
        Preprocess Funda data:
        - Clean data by removing rows that miss essential info
        """

        # remove records missing essential data    
        df = df[df.apply(self._filter_records_missing_data, axis = 1)]
        
        return df
        
    # Detect missing values for 'vraagprijs' or 'woonoppervlakte' or 'postcode_wijk'
    def _filter_records_missing_data(self, row):
        for column_name in self.required_fields:
            if self._is_missing(row[column_name]):
                return False
        return True
    
    def _is_missing(self, value):
        return isinstance(value, float) and math.isnan(value)
    
