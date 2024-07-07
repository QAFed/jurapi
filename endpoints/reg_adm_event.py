import requests
import LINKS

class RegAdmEvent:
    def __init__(self):
        self.end_point = "/journal/admin"
        self.response = None
        self.response_json = None

    def reg_adm_event(self, payload):
        self.response = requests.put(LINKS.TARGET_HOST+self.end_point,json=payload)
        self.response_json = self.response.json()