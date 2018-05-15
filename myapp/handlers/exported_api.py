
from myapp import app
from flask  import make_response
from myapp.models.Locality import Locality
import json


@app.route('/api/1/w3val/getstats', methods=['GET'])
def showPop():

    qry = Locality.query().order(-Locality.counter).fetch(3)

    mydata = []

    for each in qry:
        datadic = {}
        datadic['loc_name'] = each.name
        datadic['loc_counter'] = each.counter
        mydata.append(datadic)

    json_response = {}

    json_response['data'] = mydata
    json_response['status'] = 'OK'
    json_response['message'] = 'Successfully returned the resource.'
    response = make_response(json.dumps(json_response, ensure_ascii=True), 200)
    response.headers['content-type'] = 'application/json'
    return response
