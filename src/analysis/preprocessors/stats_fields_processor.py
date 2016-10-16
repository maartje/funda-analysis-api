class StatsFieldsProcessor:
    
    def process(self, df):
        df['ppm2'] = df['vraagprijs'] / df['woonoppervlakte']   
        df['verkoopdatum_jaar'] = df['verkoopdatum'].apply(lambda d: int(d[0:4]))
        df['verkoopdatum_maand'] = df['verkoopdatum'].apply(lambda d: int(d[5:7]))
        df['verkoopdatum_kwartaal'] = df['verkoopdatum'].apply(lambda d: self._month_to_quarter(int(d[5:7])))
        return df
        
    def _month_to_quarter(self, month):
        if month <=3:
            return 1
        if month <=6:
            return 2
        if month <=9:
            return 3
        return 4

