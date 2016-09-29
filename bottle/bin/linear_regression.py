from sklearn import linear_model

class LinearRegression:
   'Uses linear regression to predict housing prices'

   def __init__(self, feature_selector):
      self.model = linear_model.LinearRegression()
      self.feature_selector = feature_selector
      
      
   def fit(self, dataframe):
      features, targets = self.feature_selector.dataframe_to_features(dataframe)
      self.model.fit(features, targets)
      
   def predict(self, dict):
      features = self.feature_selector.dict_to_features(dict)
      predictions = self.model.predict(features)
      return predictions[0]

