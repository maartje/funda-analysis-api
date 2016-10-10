"""Model to predict the 'vraagprijs' from the features of a house"""

import numpy as np

class WrappedModel:
   """Model to predict the 'vraagprijs' from the features of a house
   
   The model transforms the provided features so that they are conform
   the features that has been used to train the model.
   """

   def __init__(self, model, feature_selector):
      """Initialize the model.
      
      model: skicit model for predicting
      feature_selector: transforms the features so that they suit the model
      """
      self.model = model
      self.feature_selector = feature_selector

   def predict(self, dict):
      """Predict 'vraagprijs' from features in dictionary."""
      features = [np.array(self.feature_selector.dict_to_features(dict))]
      predictions = self.model.predict(features)
      return predictions[0]

