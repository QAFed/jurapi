import requests
import LINKS
from deepdiff import DeepDiff
import allure
import GENERATORS

class RegAdmEvent:
    def __init__(self):
        self.end_point = "/journal/admin"
        self.response = None
        self.response_json = None
        self.mod_response = None
        self.id = None
        self.payload = None

    def reg_adm_event(self, pay_load=None):
        payload = pay_load or self.payload
        self.response = requests.put(LINKS.TARGET_HOST+self.end_point, json=payload)
        self.response_json = self.response.json()
        self.payload = payload
    def create_gen_payload(self, count_event=1, list_event=None):
        with allure.step("Create load data"):
            if list_event:
                gen_obj = GENERATORS.EventGenerator(**list_event)
            else:
                gen_obj = GENERATORS.EventGenerator()
        self.payload = gen_obj.get_dict_reg_event()
        return self.payload

    def assert_response_body(self):
        self.mod_response = self.response.json()
        self.id = self.mod_response.pop('id')
        if self.payload["extInfo"] == None:
            self.payload.pop("extInfo")
        diff = DeepDiff(self.payload, self.mod_response, ignore_order=True)
        if diff:
            with allure.step("Expect result different Actual result "):
                allure.attach(str(diff), name="Difference", attachment_type=allure.attachment_type.TEXT)
            raise AssertionError(diff)

    def validate_response(self):
        try:
            self.assert_response_body()
        except AssertionError as e:
            with allure.step("Error during assert_response_body"):
                allure.attach(str(e), name="AssertionError", attachment_type=allure.attachment_type.TEXT)
            raise
