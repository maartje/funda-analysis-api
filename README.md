## Overview
JSON REST API that exposes endpoints to run analysis functions on data from the [Funda](http://www.funda.nl/) housing website. The data is scraped starting from october 2016 and includes de regions Amsterdam, Utrecht, Rotterdam and Den Haag.

## API reference

The API exposes endpoints for summary statistics (`mean`) and machine learning models (`regression`, `nearest-neighbors`). The endpoints are described below.

#### Mean

Returns the mean for a set of selected variables, optionally grouped by another variable. For example, `/gemeente(amsterdam)/mean$select=vraagprijs&$groupby=postcode_wijk` returns the mean sales price per 4-digit postal code region. 

_Request_

    method: GET
    uri: /gemeente(<gemeente>)/mean$select=<variable> 

The `GET mean` request can be used to get the mean for selected variables
per city region (gemeente). The variables can be passed as `$select=<variable>`. Multiple variables can be passed by using multiple select parameters, i.e. `$select=<variable1>&$select=<variable2>`. Groupby and ordering are supported with the parameters `$groupby=<variable>` and `$orderby=<variable>` clauses. It is possible to use multiple `$groupby` and `$orderby` clauses.

_Response_

The output is a .json file in the following format:

    {  
       "means":[  
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

#### Linear Regression

Returns a prediction of the sales price for a house, based on its features. For example `gemeente(amsterdam)/regression?postcode=1019RR&woonoppervlakte=144` will return the predicted sales price for a house with postcode '1019 RR' and living area '144 m<sup>2<sup>' 

_Request_

    method: GET
    uri: /gemeente(<gemeente>)/regression?postcode=<postcode>&woonoppervlakte=<woonoppervlakte>

The `GET regression` request can be used to predict the sales price of a house based on its features. The features are passed as query parameters.
The following features are required: 
`postcode` as 6-character string, 
`woonoppervlakte` in m<sup>2</sup>. 
The following features are optional (not yet implemented): 
`buitenoppervlakte` in m<sup>2</sup>, 
`erfpacht_kosten` in euro's per year, 
`erfpacht_einddatum` in 'yyyy-mm-dd' format. 
Other features are not considered by the regression algorithm.

_Response_

The output is a .json file in the following format:

    { "vraagprijs" : <value> }


#### Nearest neighbors

(not implemented yet)

Returns the nearest neighbors of a house based on its features. The intention is to provide sellers and potential buyers of a house the opportunity to base their price on comparable houses.

_Request_

    method: GET
    uri: /gemeente(<gemeente>)/nearest-neighbors?postcode=<postcode>

The `GET nearest-neighbors` request can be used to get houses that are comparable to a given house, specified by its features. The features are passed as query parameters.
The following features are required: 
`postcode` as 6-character string 
The following features are optional: 
`woonoppervlakte` in m<sup>2</sup>,
`buitenoppervlakte` in m<sup>2</sup>,
`bouwjaar`,
`woning_type`,
`tuin`.
Other features are not considered by the regression algorithm.

_Response_

The output is a .json file in the following format:

    {
        "houses" : [
            /gemeente(<gemeente>)/houses/<id>,
            ...
        ]
    }

    
## Data Model

    variables:
        aangeboden_sinds,
        achterom,
        achtertuin,
        aparte_toiletten,
        badkamers,
        badkamervoorzieningen,
        balkon,
        bouwjaar,
        bouwperiode_end,
        bouwperiode_start,
        buitenruimte_oppervlakte,
        cv_ketel,
        dakterras,
        energielabel,
        externe_bergruimte_oppervlakte,
        frans_balkon,
        garage_text,
        gemeente,huisnummer,
        inhoud,
        insertion_date,
        isolatie,
        kamers,
        kelder,
        keurmerken,
        kosten_koper,
        ligging,
        ligging_tuin,
        looptijd,
        parkeergelegenheid,
        patio,periodieke_bijdrage,
        plaats,
        postcode,
        postcode_regio,
        postcode_wijk,
        schuur_of_berging,
        slaapkamers,
        soort_bouw,
        soort_dak,
        soort_woning,
        specifiek,
        straat,
        toegankelijkheid,
        tuin_rondom,
        url,verdieping,
        verkocht,
        verkoopdatum,
        verwarming,
        vliering,
        voortuin,
        voorzieningen,
        vraagprijs,
        warm_water,
        woningtype,
        woonlagen,
        woonoppervlakte,
        zijtuin,
        zolder,
        zonneterras,
        zonneterras_breedte,
        zonneterras_diepte,
        zonneterras_oppervlakte,
        inpandige_ruimte_oppervlakte,
        achtertuin_breedte,
        achtertuin_diepte,
        achtertuin_oppervlakte,
        eigendomssituatie,
        kosten_erfpacht,
        perceel_oppervlakte,
        voortuin_breedte,
        voortuin_diepte,
        voortuin_oppervlakte,
        eind_datum_erfpacht,
        zijtuin_breedte,
        zijtuin_diepte,
        zijtuin_oppervlakte,
        patio_breedte,
        patio_diepte,
        patio_oppervlakte
