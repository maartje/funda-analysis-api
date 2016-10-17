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

    def mean(self, select, groupby = None, orderby = None, ascending = True):
        """ Return summary statistics for selected column(s) in dataframe
        
        select: String or List of Strings
        groupby: String or List of Strings
        Return: dataframe or dataserie
        """
        if groupby:
            df_means = self.df.groupby(groupby)[select].mean()
        else:
            df_means =  self.df[select].mean()
        df_means.reset_index(inplace = True)
        df_means.sort(columns=orderby, axis=0, ascending=ascending, inplace=True)
        return df_means

        
