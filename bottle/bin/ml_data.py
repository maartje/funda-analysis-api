class ML_Data:
    'Provides data for (supervised) machine learning algorithms'
    
    # def __init__(self):
    #     self.data_loader = csv_data.load()
        
    # def load_data(self):
    #     self.df_houses = 

    def get_features_train(self):
        return [[2.],[4.],[6.]]
    
    def get_targets_train(self):
        return [4.1,8.3,11.6]
        
    def get_features_from_dict(self, dict):
        return [[30]]