"""Feature selector for linear regression on Funda data."""

import pandas as pd

class FeatureSelectorLinearRegression:
    """Feature selector for linear regression  on Funda data."""

    def __init__(self):
        self.feature_names = []

    def select_features_and_targets(self, df):
        """
        Return a tuple of selected features and targets as dataframe respectively dataserie.
        
        Split categorical data into binairy columns.
        Select features to train linear regression model.
        """
        
        df_features = self._select_features(df)
        ds_targets = df['vraagprijs']
        self.feature_names = df_features.columns.values
        return df_features, ds_targets

    def _select_features(self, df):
        ## Vraagprijs = ... + [wijkfactor] * woonoppervlakte 
        df_postcode_dummies = pd.get_dummies(df['postcode_wijk'])
        df_woonoppervlakte_in_wijk = df_postcode_dummies.multiply(df['woonoppervlakte'], axis='rows')
        df_features = df_woonoppervlakte_in_wijk
        return df_features
    
    def dict_to_features(self, dict):
        """Transforms a dictionary into a list with features for the linear regression model."""
        dict[dict['postcode_wijk']] = 1 * dict['woonoppervlakte'] #set value for categorical variable
        return [dict.get(key, 0) for key in self.feature_names]

#TODO
# more generalizable? i.e. postcode_wijk => split dummies ...