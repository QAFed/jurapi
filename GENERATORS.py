import random


class EventGenerator:
    def __init__(self, event_time_from=None, event_time_to=None, action_type=None, ip=None, info=None, sort_order=None,
                 admin_ids=None, session_id=None, sort_by=None, ctime=None, ext_info=None):
        self.eventTimeFrom = event_time_from or random.choice(range(0, 100))
        self.eventTimeTo = event_time_to or self.eventTimeFrom+random.choice(range(1, 100))
        self.actionType = action_type or 1
        self.ip = ip or f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        self.info = info
        self.sortOrder = sort_order or random.choice(["asc", "desc"])
        self.adminIds = admin_ids or [random.randint(1, 10) for _ in range(random.randint(1, 10))]
        self.sessionId = session_id or random.choice(["string1", "string2"])
        self.sortBy = sort_by or random.choice(["adminId", "time", "host", "sessionId"])
        self.ctime = ctime

    def get_dict_filter(self):
        return {
            'eventTimeFrom': self.eventTimeFrom,
            'eventTimeTo': self.eventTimeTo,
            'actionType': self.actionType,
            'ip': self.ip,
            'info': self.info,
            'sortOrder': self.sortOrder,
            'adminIds': self.adminIds,
            'sessionId': self.sessionId,
            'sortBy': self.sortBy
                }

    def get_dict_reg_event(self):
        return {
            "eventTypeId": 0,   # ??? 1-система, 2-администраторы, 3=пользователи ???
            "ctime": self.ctime or random.choice(range(self.eventTimeFrom, self.eventTimeTo+1)),
            "extInfo": self.info,
            "host": self.ip,
            "adminId": random.choice(self.adminIds),
            "sessionId": self.sessionId
                }

    def dict_adm_event(self):
        dict_evol = self.get_dict_reg_event()
        dict_evol["eventTypeId"] = 1
        return dict_evol






