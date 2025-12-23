import random
import string
from core.requester import Requester


def random_path(length=12):
    """
    Generate random path for baseline request
    """
    return ''.join(
        random.choice(string.ascii_lowercase + string.digits)
        for _ in range(length)
    )


class Baseline:
    def __init__(self, url):
        self.url = url.rstrip("/")
        self.req = Requester()

        # Baseline properties
        self.status = None
        self.length = None
        self.words = None
        self.lines = None
        self.text = None

        self._generate()

    def _generate(self):
        """
        Send a request to a random non-existing path
        and store baseline response properties
        """
        fake_path = random_path()
        target = f"{self.url}/{fake_path}"

        r = self.req.get(target)

        if not r:
            return

        self.status = r.status_code
        self.text = r.text
        self.length = len(r.text)
        self.words = len(r.text.split())
        self.lines = len(r.text.splitlines())

    def is_fake(self, response):
        """
        Check if response matches baseline (fake / noise)
        """
        if not response:
            return True

        # Exact match checks
        if response.status_code == self.status:
            if len(response.text) == self.length:
                return True

        return False

    def info(self):
        """
        Return baseline info for logging
        """
        return {
            "status": self.status,
            "length": self.length,
            "words": self.words,
            "lines": self.lines
        }
