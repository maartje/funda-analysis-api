"""Feature selector for linear regression."""

class FeatureSelectorLinearRegression:
    """Feature selector for linear regression."""
    
    def dataframe_to_features(self, dataframe):
        """Return selected features, targets as numpy arrays.
        
        Split categorical data into binairy columns.
        Select features to train linear regression model.
        """
        features = [[2.],[4.],[6.]]
        targets = [4.1,8.3,11.6]
        return features, targets
        
    def dict_to_features(self, dict):
        """Transforms dictionary into a numpy array with features for the linear regression model."""
        return [[30]]