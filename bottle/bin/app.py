from bottle import route, run, request
from linear_regression import LinearRegression
from ml_data import ML_Data

ml_data = ML_Data()
linear_regression = LinearRegression(ml_data)

@route('/hello')
def hello():
    return "Hello World!"

@route('/regression')
def regression():
    '/regression?postcode=1016XE&woonoppervlakte=144&buitenoppervlakte=58'
    vraagprijs = linear_regression.predict(request.query.dict)[0]
    return {'vraagprijs' : vraagprijs}




# run(host='localhost', port=8080, debug=True)
run(host='0.0.0.0', port=8080, debug=True)
# run(host='172.17.13.111', port=8080, debug=True)



