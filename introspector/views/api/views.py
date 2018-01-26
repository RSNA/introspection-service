# pylint: disable=missing-docstring
""" Views module
"""

import requests
from flask import (
    Blueprint,
    current_app,
    jsonify,
    request,
    Response,
    url_for,
)


BP = Blueprint('api', __name__, url_prefix='/api')


@BP.route('/introspect', methods=['POST'])
def api_fhir_metadata():
    fhir_base = current_app.config['API_SERVER']

    patient = request.form['patient']
    token = request.form['token']

    request_url = fhir_base + '/Patient/' + patient
    patient_fhir = requests.get(request_url, headers={
        'Accept': 'application/fhir+json',
        'Authorization': 'Bearer ' + token
    })

    if patient_fhir.status_code == 200:
        return jsonify({
            'introspected': request_url,
            'active': True,
            'patient': patient_fhir.json(),
            'scope': 'Patient/*.read'
        })
    else:
        return jsonify({
            'introspected': request_url,
            'active': False
        })
