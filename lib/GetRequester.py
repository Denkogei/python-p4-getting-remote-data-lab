import requests
import json  # Import json module to manually parse the response

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Send a GET request to the URL
        response = requests.get(self.url)
        # Raise an exception if the status code is not 200 (OK)
        response.raise_for_status()
        # Return the response as bytes (as expected in the test)
        return response.content

    def load_json(self):
        # Get the raw response body using the get_response_body method
        response_body = self.get_response_body()
        # Convert the raw response (bytes) to a JSON Python object (list/dictionary)
        return json.loads(response_body)  # Parse the raw JSON string
