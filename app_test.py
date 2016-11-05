"""
Testing for Flask Restful APP.
"""
import unittest
import json
from app import APP, SOURCE_ISOCODES, DESTINATION_ISOCODES


def is_json(myjson):
    """Method to test if something is json."""
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True


class FlaskApiTest(unittest.TestCase):
    """Class to test FlaskApi Restful App."""

    def setUp(self):
        """Setting up flask-restful app to be tested."""
        self.app = APP.test_client()

    def test_json_return(self):
        """Testing if the api would return a valid json."""
        res = self.app.get(u'/v1/countries')
        self.assertTrue(is_json(res.data))

        res = self.app.get(u'/v1/countries?target=blah')
        self.assertTrue(is_json(res.data))

        res = self.app.get(u'/v1/countries?target=source')
        self.assertTrue(is_json(res.data))

        res = self.app.get(u'/v1/countries?target=destination')
        self.assertTrue(is_json(res.data))

    def test_status_code(self):
        """Testing the expected status code of different requests."""
        res = self.app.get(u'/v1/countries')
        self.assertEqual(res.status_code, 400)

        res = self.app.get(u'/v1/countries?target=source')
        self.assertEqual(res.status_code, 200)

        res = self.app.get(u'/v1/countries?target=destination')
        self.assertEqual(res.status_code, 200)

    def test_target_message(self):
        """Testing if the api is outputting the right message."""
        res = self.app.get(u'/v1/countries')
        self.assertIn(u'Invalid request, \'target\' parameter is required '
                      'and must be equal to \'source\' or \'destination\'.',
                      res.data)

    def test_target_source(self):
        """Testing the api target=source request."""
        res = self.app.get(u'/v1/countries?target=source')
        for isocode in SOURCE_ISOCODES:
            self.assertIn(isocode, res.data)

    def test_target_destination(self):
        """Testing the api target=destination request."""
        res = self.app.get(u'/v1/countries?target=destination')
        for isocode in DESTINATION_ISOCODES:
            self.assertIn(isocode, res.data)


def main():
    """Main method to call all tests."""
    unittest.main()

if __name__ == '__main__':
    main()
