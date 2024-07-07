import requests
import LINKS
from deepdiff import DeepDiff


class RegAdmEvent:
    def __init__(self):
        self.end_point = "/journal/admin"
        self.response = None
        self.response_json = None
        self.mod_response = None
        self.id = None
        self.payload = None

    def reg_adm_event(self, payload):
        self.response = requests.put(LINKS.TARGET_HOST+self.end_point, json=payload)
        self.response_json = self.response.json()
        self.payload = payload

    def assert_response_body(self):
        self.mod_response = self.response.json()
        self.id = self.mod_response.pop('id')
        if self.payload["extInfo"] == None:
            self.payload.pop("extInfo")
        diff = DeepDiff(self.payload, self.mod_response, ignore_order=True)
        if diff:
            raise AssertionError(diff)
        assert not diff
