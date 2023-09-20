import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        contents_list=[]
        contents = json.loads(self.get_response_body())
        for content in contents:
            contents_list.append(content)
        
        return contents_list