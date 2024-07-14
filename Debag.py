
# from endpoints.reg_adm_event import RegAdmEvent

# import T_DATA

# reg_adm_ev = RegAdmEvent()
# reg_adm_ev.reg_adm_event(T_DATA.FIRST_ADM_EVENT)
# reg_adm_ev.assert_response_body()


# from endpoints.clear_db import ClearDB
# cdb = ClearDB()
# cdb.clear_db()

import endpoints.GENERATORS

new_dict = endpoints.GENERATORS.AdminFilterGenerator()
print(new_dict.get_dict())


