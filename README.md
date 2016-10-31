install bottle

run app.py

https://funda-analysis-api-maartje.c9users.io/regression?postcode=1019RR&woonoppervlakte=144&buitenoppervlakte=58&_c9_id=livepreview0&_c9_host=https://ide.c9.io

https://funda-analysis-api-maartje.c9users.io/regression?postcode=1019RR&woonoppervlakte=144&buitenoppervlakte=58

172.17.13.111:8080/hello

https://funda-analysis-api-maartje.c9users.io/summarystatistics?$select=vraagprijs&$select=woonoppervlakte&$groupby=postcode_wijk

https://funda-analysis-api-maartje.c9users.io/mean?$select=ppm2&$select=woonoppervlakte&$groupby=postcode_wijk&$orderby=ppm2

https://funda-analysis-api-maartje.c9users.io/mean?$select=ppm2&$select=looptijd&$groupby=verkoopdatum_jaar&$groupby=verkoopdatum_maand&$orderby=ppm2

TODO API
- use ODATA 
* date/time functions: year('verkoopdatum')
* function syntax: funda-data.mean
* query syntax, i.e. filters
* others: $skip, $top

- output format
{data : [
    {postcode_wijk : 1016
    jaar : 2015
    ppm2 : { mean: 5023, median: 5011, count:300},
    looptijd: {...}
    }

]}

TO READ:
http://pandas.pydata.org/pandas-docs/stable/groupby.html