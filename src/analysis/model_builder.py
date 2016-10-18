""" Builder class that implements the pipeline to construct a predictive model. """
import numpy as np
from wrapped_model import WrappedModel 

class ModelBuilder:
    """ Builder class that implements the pipeline to construct a predictive model. """
    
    def __init__(self):
        """ Constructor. """
        self._selected_variables = []
        self._data_loader = None
        self._data_processors = []
        self._feature_selector = None
        self._model = None

    def setSelectedVariables(self, selected_variables):
        """ Set variables that are used to construct the features to train the model. """
        self._selected_variables = selected_variables
    
    def setDataLoader(self, data_loader):
        """ Set data loader to load data into a pandas dataframe. """
        self._data_loader = data_loader
        
    def addDataProcessor(self, data_processor):
        """ Adds a data processor that processes the data in the dataframe. """
        self._data_processors.append(data_processor)
        
    def setFeatureSelector(self, feature_selector):
        """ Set feature selector that selects features and targets from the dataframe. """
        self._feature_selector = feature_selector

    # TODO:
    # def setSplitter(self, splitter):
    #     self.splitter = splitter

    # TODO:
    # def setEvaluator(self, splitter):
    #     self.splitter = splitter
        
    def setModel(self, model):
        """ Set skicit model for predicting a target value from features. """
        self._model = model
        
    def build(self):
        """Construct and train model on data.
        
        Return a Wrapped model that can predict the target value
        from a dictionairy of features
        """
        
        df = self._data_loader.load(self._selected_variables)
        
        for data_processor in self._data_processors:
            df = data_processor.process(df)
        
        df_features, ds_targets = self._feature_selector.select_features_and_targets(df)
        
        self._model.fit(np.array(df_features), np.array(ds_targets))
        return WrappedModel(self._model, self._feature_selector)
