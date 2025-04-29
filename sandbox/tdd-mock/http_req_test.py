import unittest
from unittest.mock import patch, MagicMock
from http_req import http_req_get
import requests


class TestHttpReq(unittest.TestCase):
    @patch('http_req.requests.get')
    def test_error_404_endpoint_not_found(self, mock_get):
        mock_execptions = requests.exceptions.HTTPError("endpoint_not_found")
        mock_execptions.response = MagicMock(status_code=404)
        mock_get.return_value.raise_for_status.side_effect = mock_execptions

        with self.assertRaises(requests.exceptions.HTTPError) as context:
            http_req_get("https://httpbin.org/status/404")

        mock_get.assert_called_once_with("https://httpbin.org/status/404")
        self.assertEqual("endpoint_not_found", str(context.exception))
        self.assertEqual(404, context.exception.response.status_code)

    @patch('http_req.requests.get')
    def test_success_http_req_get(self, mock_get):
        mock_response = MagicMock(status_code=200, text="OK")
        mock_response.json.return_value = {"available": True}
        mock_get.return_value = mock_response

        response = http_req_get("https://httpbin.org/status/200")
        mock_get.assert_called_once_with("https://httpbin.org/status/200")
        self.assertEqual(200, response.status_code)
        self.assertEqual("OK", response.text)
        self.assertEqual({"available": True}, response.json())


if __name__ == '__main__':
    unittest.main()
