"""Linear regression model to predict housing prices."""

import numpy as np

class WrappedModel:
   """Linear regression model to predict housing prices"""

   def __init__(self, model, feature_selector):
      """Initialize linear regression model."""
      self.model = model
      self.feature_selector = feature_selector

   def predict(self, dict):
      """Predict 'vraagprijs' from features in dictionary."""
      features = [np.array(self.feature_selector.dict_to_features(dict))]
      predictions = self.model.predict(features)
      return predictions[0]

