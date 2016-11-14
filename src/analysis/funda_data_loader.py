"""Dataloader that fills a dataframe with values for requested funda variables."""

import datetime
import math

class FundaDataLoader:
    """Dataloader that fills a dataframe with values for requested funda variables."""
    
    def __init__(self, data_reader):
        """Initialize FundaDataLoader."""
        self._data_reader = data_reader
        self._index_column = 'RowKey'
        self._dtype = { 
            'postcode_wijk': str
        }
        self._column_compositions = {
            'ppm2' : {'vraagprijs', 'woonoppervlakte'},
            'verkoopdatum_jaar' : {'verkoopdatum'},
            'verkoopdatum_maand' : {'verkoopdatum'},
            'verkoopdatum_kwartaal' : {'verkoopdatum'},
            'looptijd_in_dagen' : {'verkoopdatum', 'aangeboden_sinds'},
        }
        
    def load(self, selected_variables):
        """Return a dataframe for Funda data with the selected variables as columns."""
        usecolumns = {self._index_column}
        for cname in selected_variables:
            usecolumns = usecolumns.union(self._column_compositions.get(cname, {cname}))
        df = self._data_reader.get_data(columns = usecolumns, index_column = self._index_column, dtype=self._dtype)
        self._add_calculated_columns(df, selected_variables)
        return df[selected_variables]
    
    def _add_calculated_columns(self, df, selected_columns):
        if 'ppm2' in selected_columns:
            df['ppm2'] = df['vraagprijs'] / df['woonoppervlakte']
        if 'verkoopdatum_jaar' in selected_columns:
            df['verkoopdatum_jaar'] = df['verkoopdatum'].apply(lambda d: int(d[0:4]) if not self._is_missing(d) else float('NaN'))
        if 'verkoopdatum_maand' in selected_columns:
            df['verkoopdatum_maand'] = df['verkoopdatum'].apply(lambda d: int(d[5:7]) if not self._is_missing(d) else float('NaN'))
        if 'verkoopdatum_kwartaal' in selected_columns:
            df['verkoopdatum_kwartaal'] = df['verkoopdatum'].apply(lambda d: self._month_to_quarter(int(d[5:7])) if not self._is_missing(d) else float('NaN'))
        if 'looptijd_in_dagen' in selected_columns:
            df['looptijd_in_dagen'] = df.apply(self._looptijd_in_dagen, axis = 1)

    def _month_to_quarter(self, month):
        if month <=3:
            return 1
        if month <=6:
            return 2
        if month <=9:
            return 3
        return 4

    def _looptijd_in_dagen(self, row):
        if self._is_missing(row['verkoopdatum']) or self._is_missing(row['aangeboden_sinds']):
            return float('NaN')    
        verkoopdatum = datetime.datetime.strptime(row['verkoopdatum'][0:10], "%Y-%m-%d")
        aanboddatum = datetime.datetime.strptime(row['aangeboden_sinds'][0:10], "%Y-%m-%d")
        return (verkoopdatum - aanboddatum).days

    def _is_missing(self, value):
        return isinstance(value, float) and math.isnan(value)
        
        
