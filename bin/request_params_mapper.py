import re

class RequestParamsMapper:
    
    def extract_features(self, dict):
        """ Return a dictionairy with house features from the data provided by the query string 
        
        The 'dict' parameter contains a dictionary with list values, example:
        {
            'postcode' : ['1016 XE']
            'woonoppervlakte' : [144]
        }
        """
        result = {}
        result['postcode_wijk'] = self._extract_feature_value(dict, 'postcode', regex = r'\d{4}')
        result['woonoppervlakte'] = float(self._extract_feature_value(dict, 'woonoppervlakte'))
        return result
        
    def _extract_feature_value(self, dict, key, regex = None):
        val = dict.get(key, [None])[0]
        if val and regex:
            matches = re.findall(regex, val)
            return matches[0] if matches else None
        return val