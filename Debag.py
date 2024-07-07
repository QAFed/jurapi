
# from endpoints.reg_adm_event import RegAdmEvent
#
# import T_DATA
#
# reg_adm_ev = RegAdmEvent()
# reg_adm_ev.reg_adm_event(T_DATA.FIRST_ADM_EVENT)
# print(reg_adm_ev.response, reg_adm_ev.response_json)


from endpoints.clear_db import ClearDB
cdb = ClearDB()
cdb.clear_db()
