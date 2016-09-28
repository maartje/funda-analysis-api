from sklearn import linear_model

class LinearRegression:
   'Uses linear regression to predict housing prices'

   def __init__(self, ml_data):
      self.ml_data = ml_data
      self.model = linear_model.LinearRegression()
      self.model.fit(ml_data.get_features_train(), ml_data.get_targets_train())
      
   def predict(self, dict):
       features = self.ml_data.get_features_from_dict(dict)
       prediction = self.model.predict(features)
       return prediction
