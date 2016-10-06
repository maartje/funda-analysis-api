class Statistics:
    
    def __init__(self, df):
        self.df = df
    
    
    def describe(self, select, groupby = None):
        """ Return summary statistics for selected column(s) in dataframe
        
        select: String or List of Strings
        groupby: String or List of Strings
        Return: dataframe or dataserie
        """
        if groupby:
            return self.df.groupby(groupby)[select].describe()
        return self.df[select].describe()

        
