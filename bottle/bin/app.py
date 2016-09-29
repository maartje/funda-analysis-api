from bottle import route, run, request
from linear_regression import LinearRegression
from machine_learning import MachineLearning

ml = MachineLearning()
ml.initialize()

@route('/hello')
def hello():
    return "Hello World!"

@route('/regression')
def regression():
    '/regression?postcode=1016XE&woonoppervlakte=144&buitenoppervlakte=58'
    
    vraagprijs = ml.linear_regression.predict(request.query.dict)
    return {'vraagprijs' : vraagprijs}




# run(host='localhost', port=8080, debug=True)
run(host='0.0.0.0', port=8080, debug=True)
# run(host='172.17.13.111', port=8080, debug=True)



