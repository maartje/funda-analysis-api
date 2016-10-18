class Statistics:
    
    def __init__(self, fundaDataLoader):
        self._fundaDataLoader = fundaDataLoader
    
    def mean(self, select, groupby = [], orderby = [], ascending = True):
        """ Return the means for the selected variabeles

        select: List of Strings
        groupby: List of Strings
        orderby: List of Strings
        Return: dataframe
        """
        
        columns = select + groupby
        df = self._fundaDataLoader.load(columns)

        if groupby:
            df_means = df.groupby(groupby)[select].mean()
        else:
            df_means =  df[select].mean()
        df_means.reset_index(inplace = True)
        if orderby:
            df_means.sort(columns=orderby, axis=0, ascending=ascending, inplace=True)
        return df_means