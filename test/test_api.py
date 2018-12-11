# Standard library imports...
import unittest
from unittest.mock import Mock, patch

import requests
from project.services import MyAPIClient


class ClientTestCase(unittest.TestCase):

    def setUp(self):
        self.client = MyAPIClient()

    @patch('project.services.MyAPIClient._handle_http_error_404')
    @patch('project.services.requests.get')
    def test_get_http_error(self, mock_get, mock_http_error_handler_404):
        """
        Test getting a HTTP error in the _get method of MyAPIClient.
        """
        # Construct our mock response object, giving it relevant expected
        # behaviours
        mock_response = Mock()
        http_error = requests.exceptions.HTTPError()
        http_error.response = Mock()
        http_error.response.status_code = 404
        mock_response.raise_for_status.side_effect = http_error

        # Assign our mock response as the result of our patched function
        mock_get.return_value = mock_response

        url = 'http://api.chengbao.com/products/'
        self.client._get(url=url)

        # Check that our function made the expected internal calls
        mock_get.assert_called_once_with(url=url)
        self.assertEqual(1, mock_response.raise_for_status.call_count)

        # Make sure we did not attempt to deserialize the response
        self.assertEqual(0, mock_response.json.call_count)

        # Make sure our HTTP error handler is called
        mock_http_error_handler_404.assert_called_once_with(http_error)

if __name__ == "__main__":
    unittest.main()