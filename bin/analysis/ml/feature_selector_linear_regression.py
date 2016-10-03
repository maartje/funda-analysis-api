"""Feature selector for linear regression."""

import pandas as pd


class FeatureSelectorLinearRegression:
    """Feature selector for linear regression."""

    def _select_features(self, df):
        ## Vraagprijs = ... + [wijkfactor] * woonoppervlakte 
        df_postcode_dummies = pd.get_dummies(df['postcode_wijk'])
        df_woonoppervlakte_in_wijk = df_postcode_dummies.multiply(df['woonoppervlakte'], axis='rows')
        df_features = df_woonoppervlakte_in_wijk
        return df_features
    
    def select_features_and_targets(self, df):
        """Return a tuple of selected features and targets as dataframe respectively dataserie.
        
        Split categorical data into binairy columns.
        Select features to train linear regression model.
        """
        
        df_features = self._select_features(df)
        ds_targets = df['vraagprijs']
        return df_features, ds_targets
    
