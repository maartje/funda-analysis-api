""" Filter for removing duplicated records."""

import math

class FilterDuplicates:

    def process(self, df):
        """ Return a dataframe without duplicated records. """
        
        # remove duplicated records
        df = df[~df.index.duplicated()]
    
        return df
        
