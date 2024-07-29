
import endpoints.get_body_adm_filter as GAF
import GENERATORS
import endpoints.clear_db as CDB

# clr = CDB.ClearDB()
# clr.clear_db()

load = GAF.GetFiltAdmEvent()
load.load_true_fiter_events(count_event=2)
load.get_adm_events()
