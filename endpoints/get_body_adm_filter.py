import requests
import LINKS
import GENERATORS
from deepdiff import DeepDiff


class GetFiltAdmEvent:
    def __init__(self):
        self.end_point = "/journal/admin"  # на тот же адрес как регистрация только post
        self.page = None
        self.page_size = None
        self.response = None
        self.response_json = None
        self.mod_response = None
        self.id = None
        self.payload = None

    def reg_adm_event(self, payload):
        self.response = requests.post(LINKS.TARGET_HOST+self.end_point, json=payload)
        self.response_json = self.response.json()
        self.payload = payload

    def load_true_fiter_events(self, count_env, list_env=None):
        if list_env:
            fiter_event = GENERATORS.EventGenerator(**list_env)
        else:
            fiter_event = GENERATORS.EventGenerator()
        for n in range(1,count_env+1):
            self.reg_adm_event(fiter_event.dict_adm_event())

    # def assert_response_body(self):
    #     self.mod_response = self.response.json()
    #     self.id = self.mod_response.pop('id')
    #     if self.payload["extInfo"] == None:
    #         self.payload.pop("extInfo")
    #     diff = DeepDiff(self.payload, self.mod_response, ignore_order=True)
    #     if diff:
    #         raise AssertionError(diff)
    #     assert not diff
