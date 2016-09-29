""" Clean and transform Funda data."""

import math

# Detect missing values for 'vraagprijs' or 'woonoppervlakte' or 'postcode_wijk'
def _filter_records_missing_data(row):
    for column_name in ['vraagprijs', 'woonoppervlakte', 'postcode_wijk']:
        if _is_missing(row[column_name]):
            return False
    return True

def _is_missing(value):
    return isinstance(value, float) and math.isnan(value)

def preprocess(df):
    """ Return a dataframe with cleaned Funda data.
    
    Preprocess Funda data:
    - Clean data by removing rows that miss essential info
    - Construct new columns that contain aggregated data or data in other format
    - Drop columns that are irrelevant
    """
    
    # remove duplicates
    df = df[~df.index.duplicated()]

    # filter records missing essential data    
    df = df[df.apply(_filter_records_missing_data, axis = 1)]
    
    # set type of postcode wijk to string
    df['postcode_wijk'] = df['postcode_wijk'].apply(lambda p: str(p))

    return df