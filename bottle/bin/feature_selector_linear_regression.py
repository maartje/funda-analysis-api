# dataframe => dataframe
# split categorical data into binairy columns
# select columns for ML algorithm

class FeatureSelectorLinearRegression:
    'Selects the features for the linear regression model'
    
    def dataframe_to_features(self, dataframe):
        features = [[2.],[4.],[6.]]
        targets = [4.1,8.3,11.6]
        return features, targets
        
    def dict_to_features(self, dict):
        return [[30]]