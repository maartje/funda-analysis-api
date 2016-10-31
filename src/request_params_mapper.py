import re

class RequestParamsMapper:
    
    def get_select(self, dict):
        return dict.get('$select', None)
    
    def get_groupby(self, dict):
        return dict.get('$groupby', None)
    
    def get_orderby(self, dict):
        return dict.get('$orderby', None)

    # def get_filter(self, dict):
    #     filter = dict.get('$filter', None)
    #     # "gemeente eq Amsterdam"
    #     return filter

    
    def get_funda_variables(self, dict):
        """ Return a dictionairy with funda variables from the data provided by the query string 
        
        The 'dict' parameter contains a dictionary with list values, example:
        {
            'postcode' : ['1016 XE']
            'woonoppervlakte' : [144]
        }
        """
        result = {}
        result['postcode_wijk'] = self._extract_variable_value(dict, 'postcode', regex = r'\d{4}')
        result['woonoppervlakte'] = float(self._extract_variable_value(dict, 'woonoppervlakte'))
        return result
        
    def _extract_variable_value(self, dict, key, regex = None):
        val = dict.get(key, [None])[0]
        if val and regex:
            matches = re.findall(regex, val)
            return matches[0] if matches else None
        return val