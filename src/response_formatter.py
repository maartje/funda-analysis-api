import pandas as pd

# TODO: think of more generic utility functions to format the dict/JSON output
# TODO: return dict from statistics, reformat the dict here?!
def dataframe_to_dict(df):
    if isinstance(df.index, pd.core.index.MultiIndex):
        return _multi_index_to_dict(df)
    return df.to_dict()

def _multi_index_to_dict(df_multi_index):
    dict_result = {}
    for k in df_multi_index.index:
        groupkey = k[:-1]
        key = ' '.join(map(str, groupkey))
        value = df_multi_index.loc[groupkey].to_dict()
        dict_result[key] = value
    return dict_result
