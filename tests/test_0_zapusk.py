from endpoints.get_body_adm_filter import GetFiltAdmEvent
# import allure

def test_zap_get_by_filter():
    ent_for_filter = GetFiltAdmEvent()
    ent_for_filter.load_true_fiter_events()
    ent_for_filter.get_adm_events()
    ent_for_filter.assert_response_body()
