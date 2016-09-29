"""Linear regression model to predict housing prices."""

from sklearn import linear_model

class LinearRegression:
   """Linear regression model to predict housing prices"""

   def __init__(self, feature_selector):
      """Initialize linear regression model."""
      self.model = linear_model.LinearRegression()
      self.feature_selector = feature_selector
      
      
   def fit(self, dataframe):
      """Train linear regression model on funda data."""
      features, targets = self.feature_selector.dataframe_to_features(dataframe)
      self.model.fit(features, targets)
      
   def predict(self, dict):
      """Predict 'vraagprijs' using linear regression."""
      features = self.feature_selector.dict_to_features(dict)
      predictions = self.model.predict(features)
      return predictions[0]

