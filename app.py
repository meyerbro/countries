"""
Flask Restful APP to return json lists of source and destination countries.
"""
from flask import Flask, abort
from flask_restful import Resource, Api, reqparse
import pycountry


APP = Flask(__name__)
API = Api(APP)


COUNTRIES = pycountry.countries
SOURCE_ISOCODES = [u'GB', u'FR']
DESTINATION_ISOCODES = [u'GB', u'FR', u'IE', u'ES']


class FlaskApi(Resource):
    """Flask Restful API class for source and destination countries."""

    def get(self):
        """Service to retrive source or destination countries."""

        parser = reqparse.RequestParser()
        parser.add_argument(
            u'target', required=True, type=str,
            choices=(u'source', u'destination'),
            help=u'Invalid request, \'target\' parameter is required '
            'and must be equal to \'source\' or \'destination\'.')
        args = parser.parse_args()

        if args[u'target'] == u'source':
            return [{'name': c.name, 'isoCode': c.alpha2}
                    for c in COUNTRIES if c.alpha2 in SOURCE_ISOCODES]
        elif args[u'target'] == u'destination':
            return [{'name': c.name, 'isoCode': c.alpha2}
                    for c in COUNTRIES if c.alpha2 in DESTINATION_ISOCODES]
        else:
            abort(400)

API.add_resource(FlaskApi, '/v1/countries')

if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0', port=80)
