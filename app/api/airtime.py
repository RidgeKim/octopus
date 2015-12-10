from app import app
from flask import (request, make_response)


@app.route('/api/airtime/dlr/', methods=['POST'])
def airtime_dlr_callback():
    if request.method == 'POST':

        # Reads the variables sent via POST from our gateway
        _from = request.values.get('from', None)
        to = request.values.get('to', None)
        id_ = request.values.get('text', None)

        print id_, _from, to

        resp = make_response('Ok', 200)
        resp.headers['Content-Type'] = 'application/json'
        resp.cache_control.no_cache = True
        return resp
    else:
        resp = make_response('Error', 400)
        resp.headers['Content-Type'] = 'application/json'
        resp.cache_control.no_cache = True
        return resp