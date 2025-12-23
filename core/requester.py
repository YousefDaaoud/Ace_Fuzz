import requests

class Requester:
    def __init__(self, timeout=5):
        self.timeout = timeout
        self.session = requests.Session()

    def get(self, url, headers=None):
        try:
            r = self.session.get(
                url,
                headers=headers,
                timeout=self.timeout,
                allow_redirects=False
            )
            return r
        except requests.RequestException:
            return None
