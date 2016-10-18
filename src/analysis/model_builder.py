""" Builder class that implements the pipeline to construct a predictive model. """
import numpy as np
from wrapped_model import WrappedModel 

class ModelBuilder:
    """ Builder class that implements the pipeline to construct a predictive model. """
    
    def __init__(self):
        """ Constructor. """
        self.selected_variables = []
        self.data_loader = None
        self.data_processors = []
        self.feature_selector = None
        self.model = None

    def setSelectedVariables(self, selected_variables):
        self.selected_variables = selected_variables
    
    def setDataLoader(self, data_loader):
        """ Set data reader to read data into a pandas dataframe. """
        self.data_loader = data_loader
        
    def addDataProcessor(self, data_processor):
        """ Adds a data processor that processes the data in the dataframe. """
        self.data_processors.append(data_processor)
        
    def setFeatureSelector(self, feature_selector):
        """ Set feature selector that selects features and targets from the dataframe. """
        self.feature_selector = feature_selector

    # TODO:
    # def setSplitter(self, splitter):
    #     self.splitter = splitter

    # TODO:
    # def setEvaluator(self, splitter):
    #     self.splitter = splitter
        
    def setModel(self, model):
        """ Set skicit model for predicting a target value from features. """
        self.model = model
        
    def build(self):
        """Construct and train model on data.
        
        Return a Wrapped model that can predict the target value
        from a dictionairy of features
        """
        
        df = self.data_loader.load(self.selected_variables)
        
        for data_processor in self.data_processors:
            df = data_processor.process(df)
        
        df_features, ds_targets = self.feature_selector.select_features_and_targets(df)
        
        self.model.fit(np.array(df_features), np.array(ds_targets))
        return WrappedModel(self.model, self.feature_selector)
