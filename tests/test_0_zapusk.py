import random
import pytest
from endpoints.get_adm_event_by_filter import GetFiltAdmEvent
# import allure

# @pytest.mark.usefixtures("pre_clear")
@pytest.mark.parametrize('gen_list', [
    {'ip':"121212"},
    {'ip':f"{random.randint(0,10)}"},
    {'ip':"161616"}
], ids=lambda x: str(x))
def test_adm_event_get_by_filter(gen_list):
    ent_for_filter = GetFiltAdmEvent()
    ent_for_filter.load_true_fiter_events(list_event=gen_list)
    ent_for_filter.get_adm_events()
    ent_for_filter.assert_response_body()


