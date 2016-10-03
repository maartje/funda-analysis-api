import re

def request_params_to_features(dict):
    """ Return a dictionairy with house features from the data provided by the query string 
    
    The 'dict' parameter contains a dictionary with list values, example:
    {
        'postcode' : ['1016 XE']
        'woonoppervlakte' : [144]
    }
    """
    result = {}
    result['postcode_wijk'] = _extract_feature_value(dict, 'postcode', regex = r'\d{4}')
    result['woonoppervlakte'] = float(_extract_feature_value(dict, 'woonoppervlakte'))
    return result
    
def _extract_feature_value(dict, key, regex = None):
    val = dict.get(key, [None])[0]
    if val and regex:
        matches = re.findall(regex, val)
        return matches[0] if matches else None
    return val