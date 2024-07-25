
import endpoints.get_body_adm_filter as GAF

load = GAF.GetFiltAdmEvent()
load.load_true_fiter_events(count_event=2)
load.get_adm_events()

