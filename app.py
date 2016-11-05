"""
Python Flask APP to return json lists of source and destination countries
"""

from flask import Flask, jsonify, abort
from flask_restful import Resource, Api, reqparse

import pycountry


APP = Flask(__name__)
API = Api(APP)


COUNTRIES = pycountry.countries
SOURCE_ISOCODES = [u'GB', u'FR']
DESTINATION_ISOCODES = [u'GB', u'FR', u'IE', u'ES']


class FlaskApi(Resource):
    """Flask Restful API class for source and destination countries."""

    @staticmethod
    def format_country(country):
        """Return a formatted country (name, isocode)."""
        return {"name": country.name, u'isoCode': country.alpha2}

    def formatted_json(self, country_list):
        """Return a json with a list of formatted countries."""
        formatted_list = []
        for iso_code in country_list:
            formatted_country = self.format_country(
                COUNTRIES.get(alpha2=iso_code))
            formatted_list.append(formatted_country)
        return jsonify(formatted_list)

    def get(self):
        """Service to retrive source or destination countries."""

        parser = reqparse.RequestParser()
        parser.add_argument(u'target', required=True, type=str,
                            help=u'Target cannot be blank.')
        args = parser.parse_args()

        if args[u'target'] == u'source':
            return self.formatted_json(SOURCE_ISOCODES)
        elif args[u'target'] == u'destination':
            return self.formatted_json(DESTINATION_ISOCODES)
        else:
            abort(400)

        # target_arg = request.args.get(u'target')
        # if target_arg == u'source':
        #     return formatted_json(SOURCE_ISOCODES)
        # elif target_arg == 'destination':
        #     return formatted_json(DESTINATION_ISOCODES)
        # else:
        #     abort(400)


API.add_resource(FlaskApi, '/v1/countries')

if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0')
