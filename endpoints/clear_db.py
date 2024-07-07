import requests
import LINKS


class ClearDB:
    def __init__(self):
        self.end_point = "/clearDB"
        self.response = None

    def clear_db(self):
        self.response = requests.post(LINKS.TARGET_HOST+self.end_point)
