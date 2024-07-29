import requests
import LINKS
import GENERATORS
from deepdiff import DeepDiff


class GetFiltAdmEvent:
    def __init__(self):
        self.end_point = "/journal/admin"  # на тот же адрес как регистрация только post
        self.page = 0
        self.page_size = 10
        self.response = None
        self.response_json = None
        self.mod_response = None
        self.id = None
        self.payload = None
        self.filtered_list_events = None
        self.fiter_dody = None
        self.urez_fiter_dody = None


    def reg_adm_event(self, payload):
        response = requests.put(LINKS.TARGET_HOST+self.end_point, json=payload)
        response_json = response.json()
        print("загрузка payload", payload)
        return response_json

    def load_true_fiter_events(self, count_event=1, list_event=None):
        if list_event:
            fiter_event = GENERATORS.EventGenerator(**list_event)
        else:
            fiter_event = GENERATORS.EventGenerator()

        nofiter_list_events = []
        self.fiter_dody = fiter_event.get_dict_filter()


        for n in range(1, count_event+1):
            dict_adm_body = fiter_event.dict_adm_event()
            response = self.reg_adm_event(dict_adm_body)
            mod_dict_event = {k: v for k, v in dict_adm_body.items() if v is not None}
            mod_dict_event['id'] = response['id']
            nofiter_list_events.append(mod_dict_event)
            if fiter_event.sortBy == 'time':
                fiter_sort_by = 'ctime'
            else:
                fiter_sort_by = fiter_event.sortBy
        self.filtered_list_events = sorted(nofiter_list_events, key=lambda x: x[fiter_sort_by], reverse=fiter_event.sortOrder=="desc")
        print("фильтрованный эталонный список", self.filtered_list_events)

    # def etalon_page(self):
    #     len_list = len(self.filtered_list_events)
    #     if len_list%self.page == 0 or len_list//self.page_size != self.page:
    #         return self.filtered_list_events[self.page_size*(self.page-1):self.page_size*self.page:]
    #     else:
    #         return self.filtered_list_events[self.page_size * (self.page - 1):self.page_size * (self.page - 1+len_list%self.page):]

    def get_adm_events(self, payload=None, page = None, pageSize = None):
        in_payload = payload or self.fiter_dody
        in_page = page or self.page
        in_page_size = pageSize or self.page_size
        response = requests.post(LINKS.TARGET_HOST + self.end_point, json=in_payload, params= {'page': in_page, 'pageSize': in_page_size})
        response_json = response.json()
        print("загрузка фильтра payload", in_payload)
        print('ответ сервера по фильтру', response_json)
        return response_json





    # def assert_response_body(self):
    #     self.mod_response = self.response.json()
    #     self.id = self.mod_response.pop('id')
    #     if self.payload["extInfo"] == None:
    #         self.payload.pop("extInfo")
    #     diff = DeepDiff(self.payload, self.mod_response, ignore_order=True)
    #     if diff:
    #         raise AssertionError(diff)
    #     assert not diff
