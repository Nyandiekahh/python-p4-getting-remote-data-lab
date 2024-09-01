import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Send GET request to the URL
        response = requests.get(self.url)
        # Ensure the request was successful
        response.raise_for_status()
        # Return the response body as bytes
        return response.content

    def load_json(self):
        # Get the response body
        response_body = self.get_response_body()
        # Convert response body from JSON to Python list or dictionary
        return json.loads(response_body.decode('utf-8'))
