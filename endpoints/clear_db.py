import requests
import LINKS


class ClearDB:
    end_point = "/clearDB"
    response = None

    def clear_db(self):
        self.response = requests.post(LINKS.TARGET_HOST+self.end_point)
        return self.response
