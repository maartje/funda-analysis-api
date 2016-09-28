from bottle import route, run, request

class LinearRegression:
   'Uses linear regression to predict housing prices'

   def __init__(self):
      self.model = "TODO"
      print "model trained ..."

   def predict(self, house):
     print "predicting ..." + str(house)
     return 625000


linear_regression = LinearRegression()

@route('/hello')
def hello():
    return "Hello World!"

@route('/regression')
def regression():
    '/regression?postcode=1016XE&woonoppervlakte=144&buitenoppervlakte=58'
    postcode = request.query.postcode
    woonoppervlakte = request.query.woonoppervlakte
    
    house = { 
        'woonoppervlakte' : woonoppervlakte,
        'postcode' : postcode
    }
    house['vraagprijs'] = linear_regression.predict(house)
    return house;




# run(host='localhost', port=8080, debug=True)
# run(host='0.0.0.0', port=8080, debug=True)
run(host='172.17.13.111', port=8080, debug=True)



