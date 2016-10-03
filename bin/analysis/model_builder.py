import numpy as np
from wrapped_model import WrappedModel 

class ModelBuilder:
    
    def __init__(self):
        self.data_reader = None
        self.data_processors = []
        self.feature_selector = None
        self.model = None

    
    def setDataReader(self, data_reader):
        self.data_reader = data_reader
        
    def addDataProcessor(self, data_processor):
        self.data_processors.append(data_processor)
        
    def setFeatureSelector(self, feature_selector):
        self.feature_selector = feature_selector

    # def setSplitter(self, splitter):
    #     self.splitter = splitter

    # def setEvaluator(self, splitter):
    #     self.splitter = splitter
        
    def setModel(self, model):
        self.model = model
        
    def build(self):
        """Fit model on data."""
        df = self.data_reader.get_data()
        
        for data_processor in self.data_processors:
            df = data_processor.process(df)
        
        df_features, ds_targets = self.feature_selector.select_features_and_targets(df)
        
        self.model.fit(np.array(df_features), np.array(ds_targets))
        print "fit"
        return WrappedModel(self.model, self.feature_selector)
