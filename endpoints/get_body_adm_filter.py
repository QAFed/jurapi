import requests
import LINKS
import GENERATORS
from deepdiff import DeepDiff


class GetFiltAdmEvent:
    def __init__(self):
        self.end_point = "/journal/admin"  # на тот же адрес как регистрация только post
        self.page = 0
        self.page_size = 0
        self.response = None
        self.response_json = None
        self.mod_response = None
        self.id = None
        self.payload = None
        self.filtered_list_events = None

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
            dict_event = fiter_event.dict_adm_event()
            self.reg_adm_event(dict_event)
            nofiter_list_events = []
            nofiter_list_events.append(dict_event)
            self.filtered_list_events = sorted(nofiter_list_events, key=lambda x: x[fiter_event.sortBy],reverse=fiter_event.sortOrder=="desc")

    def etalon_page(self):
        len_list = len(self.filtered_list_events)
        if len_list%self.page == 0 or len_list//self.page_size != self.page:
            return self.filtered_list_events[self.page_size*(self.page-1):self.page_size*self.page:]
        else:
            return self.filtered_list_events[self.page_size * (self.page - 1):self.page_size * (self.page - 1+len_list%self.page):]







    # def assert_response_body(self):
    #     self.mod_response = self.response.json()
    #     self.id = self.mod_response.pop('id')
    #     if self.payload["extInfo"] == None:
    #         self.payload.pop("extInfo")
    #     diff = DeepDiff(self.payload, self.mod_response, ignore_order=True)
    #     if diff:
    #         raise AssertionError(diff)
    #     assert not diff
