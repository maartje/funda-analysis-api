## Overview
JSON REST API exposing analysis functions on data from the [Funda](http://www.funda.nl/) housing website. The data is collected starting from october 2016 and includes de regions Amsterdam, Utrecht, Rotterdam and Den Haag.

## Motivation
This Web API is part of a study project to learn data science. The main learning purposes: Python, pandas, numpy, scikit-learn, predictive models, API development.

## Getting Started

install [bottle](http://bottlepy.org/docs/dev/), [pandas](http://pandas.pydata.org/), [scikit-learn](http://scikit-learn.org/stable/) and [azure-storage](https://github.com/Azure/azure-storage-python)

run app.py

## API reference

The API exposes endpoints for summary statistics and machine learning models as listed below. 

|        | Description |
| ------ | ----------- |
| `mean`   | Returns the [mean](#mean) for a set of selected variabeles, optionally grouped and ordered. Example:               <br> `/amsterdam/mean?$select=ppm2&$groupby=postcode_wijk` |
| `linear regression` | Returns a prediction of the sales price of a house using [regression](#regression).                  Example:  <br> `amsterdam/regression?postcode=1019RR&woonoppervlakte=144`|
| `k-nearest-neighbors`    | Returns a prediction of the sales price based on similar houses. See [k-nearest-neighbors](#nearest-neighbors). Example: <br>                                  `amsterdam/nearest-neighbors?postcode=1019RR&woonoppervlakte=144&bouwjaar=1995`|

<a name="mean"></a>
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

<a name="regression"></a>
#### Regression

The `GET regression` request returns a prediction of the sales price for a house based on its features passed as query parameters. For example `amsterdam/regression?postcode=1019RR&woonoppervlakte=144` will return the predicted sales price for a house with postcode '1019 RR' and living area '144 m<sup>2</sup>'. 
`postcode` and `woonoppervlakte` are required features.
Optional features are ... (not implemented yet).


_Request_

    method: GET
    uri: /<gemeente>/regression?postcode=<postcode>&woonoppervlakte=<woonoppervlakte>&...


_Response_

    { "vraagprijs" : <value> }



<a name="nearest-neighbors"></a>
#### Nearest neighbors

(not implemented yet)

The `GET nearest-neighbors` request returns a prediction of the price based on houses with features that are similar to those passed in the query parameters. The intention is to provide sellers and buyers of a house the opportunity to compare similar houses. Features that are used for comparison:
`postcode`,
`woonoppervlakte`,
`buitenoppervlakte`,
`bouwjaar`,
`woning_type`,
`tuin`.
The `$select` option can be used to specify a subset of housing features to include in the response.


_Request_

    method: GET
    uri: /<gemeente>/nearest-neighbors?feature=<feature>&...&$select=<feature>&...

_Response_

    {  
       "vraagprijs" : <value>,
       "houses" : [ ... ]
    }



## Data Model

**url** : *String* <br>


<!--locatie-->

**gemeente** : *string {amsterdam, denhaag, rotterdam, utrecht}*
**huisnummer**  : *String*<br>
**postcode**  : *String [\d{4} [a-z]{2}]*<br>
**postcode_regio**  : *String [\d{2}]*<br>
**postcode_wijk**  : *String [\d{4}]*<br>
**straat**  : *String* <br>


<!--vraagprijs-->

**vraagprijs**  : *Number*<br>
**kosten_koper**  : *Boolean*<br>
**ppm2** : *Number* <br>


<!--oppervlakte--> 

**woonoppervlakte** : *Number* <br>
**perceel_oppervlakte** : *Number* <br>
**inhoud** : *Number* <br>


<!--soort woning-->

**soort_woning** : *String* <br>
**verdieping** : *Number*  <br>
**woningtype** : *String {huis, appartement}* <br>
**woonlagen** <br>
**bouwjaar** : *Number* <br>
**bouwperiode_end** : *Number* <br>
**bouwperiode_start** : *Number* <br>


<!--verkoop-->

**aangeboden_sinds** : *String [yyyy-mm-dd]* <br>
**verkocht** : *Boolean* <br>
**verkoopdatum** : *String [yyy-mm-dd]* <br>
**looptijd** : *String* <br>
**verkoopdatum_jaar** : : *Number* <br>
**verkoopdatum_maand** : : *Number* <br>
**verkoopdatum_kwartaal** : *Number* <br>
**looptijd-in-dagen**  : *Number*<br>


<!--bergruimte-->

**externe-bergruimte-oppervlakte**  : *Number*<br>
**inpandige-ruimte-oppervlakte** : *Number* <br>
**zolder** : *Boolean* <br>
**kelder** : *Boolean* <br>
**schuur-of-berging** : *Boolean* <br>
**vliering** : *Boolean* <br>
**garage-text** : *String* <br>


<!--kenmerken-->

**aparte_toiletten** : *Number* <br>
**badkamers**        : *Number* <br>
**badkamervoorzieningen** : *String* <br>
**kamers**  : *Number*<br>
**slaapkamers**  : *Number*<br>
**energielabel**  : *String {A, B, C, D, E, F, G}*<br>






<!--erfpacht-->

**eigendomssituatie** : *String* <br>
**kosten_erfpacht** : *Number* <br>
**eind-datum-erfpacht** : *String [yyyy-mm-dd]* <br>


<!--buitenruimte-->

**buitenruimte-oppervlakte** : *Number* <br>
**balkon** : *Boolean* <br>
**dakterras** : *Boolean* <br>
**tuin** : *Boolean* <br>
**zonneterras** : *Boolean* <br>
**patio** : *Boolean* <br>
**plaats** : *Boolean* <br>



