
import endpoints.get_adm_event_by_filter as GAF
import GENERATORS
import endpoints.clear_db as CDB

# clr = CDB.ClearDB()
# clr.clear_db()

load = GAF.GetFiltAdmEvent()
load.load_true_fiter_events(count_event=3)
load.get_adm_events()
print(load.etalon_page())
load.assert_response_body()