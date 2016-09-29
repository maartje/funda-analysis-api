import re

class RequestParamsMapper:
    
    def extract_features(self, dict):
        result = {}
        result['postcode_wijk'] = re.findall(r'\d{4}', dict.get('postcode', [''])[0])[0]
        result['woonoppervlakte'] = dict.get('woonoppervlakte', [None])[0]
        return result