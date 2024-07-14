import random


class AdminFilterGenerator:
    def __init__(self, event_time_from=None, event_time_to=None, action_type=None, ip=None, info=None, sort_order=None,
                 admin_ids=None, session_id=None, sort_by=None):
        self.eventTimeFrom = event_time_from or random.choice(range(0, 100))
        self.eventTimeTo = event_time_to or self.eventTimeFrom+random.choice(range(0, 100))
        self.actionType = action_type or random.choice(range(1, 10))
        self.ip = ip or f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        self.info = info or random.choice(["string1", "string2"])
        self.sortOrder = sort_order or random.choice(["asc", "desc"])
        self.adminIds = admin_ids or [random.randint(1, 10) for _ in range(random.randint(1, 10))]
        self.sessionId = session_id or random.choice(["string1", "string2"])
        self.sortBy = sort_by or random.choice(["id", "time", "host", "info", "sessionId"])

    def get_dict(self):
        return {'eventTimeFrom': self.eventTimeFrom,
                'eventTimeTo': self.eventTimeTo,
                'actionType': self.actionType,
                'ip': self.ip,
                'info': self.info,
                'sortOrder': self.sortOrder,
                'adminIds': self.adminIds,
                'sessionId': self.sessionId,
                'sortBy': self.sortBy
                }
