# Standard library imports...
from urllib.parse import urljoin

# Third-party imports...
import requests

# Local imports...
from project.constants import BASE_URL, VERSION

# client.py
import requests

class MyAPIClient(object):
    """A simple API client for querying corgi data"""

    def _make_uri(self, resource):
        """
        Construct the URL for a resource based on the API class's parameters
        """
        return '/'.join([BASE_URL, VERSION, resource])

    def _get(self, url):
        """Make a GET request to an endpoint defined by 'url'"""
        response = requests.get(url=url)
        try:
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                self._handle_http_error_404(e)
            else:
                self._handle_http_error(e)

    def get_product_info(self, product):
        """Return information about a specific product"""
        resource = '/'.join(['productsd', product])
        url = self._make_url(resource=resource)
        response = self._get(url=url)
        return response

    def _handle_http_error(self, e):
        """Handle a HTTP error"""
        if e.response.status_code == 404:
            self._handle_http_error_404(e)

    def _handle_http_error_404(self, e):
        pass