"""Linear regression model to predict housing prices."""

from sklearn import linear_model
import numpy as np

class LinearRegression:
   """Linear regression model to predict housing prices"""

   def __init__(self, feature_selector):
      """Initialize linear regression model."""
      self.model = linear_model.LinearRegression()
      self.feature_selector = feature_selector
      self.feature_names = np.array([])
      
      
   def fit(self, df):
      """Train linear regression model on funda data."""
      df_features, ds_targets = self.feature_selector.select_features_and_targets(df)
      self.feature_names = df_features.columns.values
      self.model.fit(np.array(df_features), np.array(ds_targets))
      
   def predict(self, dict):
      """Predict 'vraagprijs' using linear regression."""
      features = self._dict_to_features(dict)
      predictions = self.model.predict(features)
      return predictions[0]

   def _dict_to_features(self, dict):
        """Transforms dictionary into a numpy array with features for the linear regression model."""
        dict[dict['postcode_wijk']] = 1 * float(dict['woonoppervlakte']) #set value for categorical variable
        feature_array = np.array([dict.get(key, 0) for key in self.feature_names]) #create feature array with values from dict and default values
        print feature_array
        return [feature_array]
