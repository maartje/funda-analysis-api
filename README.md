## Overview
JSON REST API that exposes endpoints to run analysis functions on data from the [Funda](http://www.funda.nl/) housing website. The data is scraped starting from october 2016 and includes de regions Amsterdam, Utrecht, Rotterdam and Den Haag.

## Getting Started

install [bottle](http://bottlepy.org/docs/dev/), [pandas](http://pandas.pydata.org/) and [scikit-learn](http://scikit-learn.org/stable/)

run app.py

## API reference

The API exposes endpoints for summary statistics and machine learning models as listed below. 

|        | Description |
| ------ | ----------- |
| `mean`   | Returns the [mean](#Mean) for a set of selected variabeles, optionally grouped and ordered. Example:               <br> `/amsterdam/mean?$select=ppm2&$groupby=postcode_wijk` |
| `regression` | Returns a prediction of the sales price of a house using [regression](#Regression).                  Example:  <br> `amsterdam/regression?postcode=1019RR&woonoppervlakte=144`|
| `nearest-neighbors`    | Returns similar houses using [k-nearest-neighbors](#Nearest-neighbors). Example: <br>                                  `amsterdam/nearest-neighbors?postcode=1019RR&woonoppervlakte=144&bouwjaar=1995`|


#### Mean

The `GET mean` request returns the mean for a set of selected variables
in a city region (gemeente), optionally grouped and ordered. For example, `/amsterdam/mean$select=vraagprijs&$groupby=postcode_wijk` returns the mean sales price for all 4-digit postal code regions. Multiple variables can be passed by using multiple select, groupby or ordering parameters, i.e. `$select=<variable1>&$select=<variable2>`.

_Request_

    method: GET
    uri: /<gemeente>/mean$select=<variable>&$groupby=<variable>&$orderby=<variable> 

_Response_

    {  
       "means" : [  
          {  
             <$select> : <value>,
             ...
             <$select> : <value>,
             <$groupby> : <value>,
             ...
             <$groupby> : <value>
          },
          ...
        ]
    }

#### Regression

The `GET regression` request returns a prediction of the sales price for a house based on its features passed as query parameters. For example `amsterdam/regression?postcode=1019RR&woonoppervlakte=144` will return the predicted sales price for a house with postcode '1019 RR' and living area '144 m<sup>2</sup>'. 
`postcode` and `woonoppervlakte` are required features.
Optional features are ... (not implemented yet).


_Request_

    method: GET
    uri: /<gemeente>/regression?postcode=<postcode>&woonoppervlakte=<woonoppervlakte>&...


_Response_

    { "vraagprijs" : <value> }


#### Nearest neighbors

(not implemented yet)

The `GET nearest-neighbors` request returns houses that have features that are similar to those passed in the query parameters. The intention is to provide sellers and buyers of a house the opportunity to compare similar houses. Features that are used for comparison:
`postcode`,
`woonoppervlakte`,
`buitenoppervlakte`,
`bouwjaar`,
`woning_type`,
`tuin`.
The `$select` option can be used to specify a subset of features to include in the response.


_Request_

    method: GET
    uri: /<gemeente>/nearest-neighbors?feature=<feature>&...&$select=<feature>&...

_Response_

    {  
       "houses" : [ ... ]
    }


#### Houses

(not implemented yet)

_Request_

    method: GET
    uri: /<gemeente>/houses??$filter=postcode_wijk eq '1016XE'$select=<feature>

_Response_

    {  
       "houses" : [ ... ]
    }
    
## Data Model

**aangeboden_sinds** : *String [yyyy-mm-dd]* <br>
**bouwjaar** : *Number* <br>
**bouwperiode_end** : *Number* <br>
**bouwperiode_start** : *Number* <br>
energielabel,
garage_text,


looptijd,
soort_woning,
url,
verdieping,
verkocht,
verkoopdatum,
vliering,
woningtype,
woonlagen,
woonoppervlakte,
perceel_oppervlakte,

<!--bergruimte-->
externe_bergruimte_oppervlakte,
inpandige_ruimte_oppervlakte,
zolder,
kelder,
schuur_of_berging,

<!--kenmerken-->
**aparte_toiletten** : *Number* <br>
**badkamers**        : *Number* <br>
**badkamervoorzieningen** : *String* <br>
kamers,
slaapkamers,

<!--vraagprijs-->
vraagprijs,
kosten_koper,

<!--locatie-->
**gemeente** : *string {amsterdam, denhaag, rotterdam, utrecht}*
huisnummer,
postcode,
postcode_regio,
postcode_wijk,
straat,

<!--erfpacht-->
eigendomssituatie,
kosten_erfpacht,
eind_datum_erfpacht,

<!--buitenruimte-->
buitenruimte_oppervlakte,
**balkon** : *Boolean* <br>
dakterras 
tuin
zonneterras,
patio,
plaats
