import json
import os
from datetime import datetime


class OutputManager:
    def __init__(self, mode):
        self.mode = mode
        self.results = []
        self.start_time = datetime.now()

        os.makedirs("output", exist_ok=True)

    def add(self, data: dict):
        self.results.append(data)

    def save(self):
        timestamp = self.start_time.strftime("%Y%m%d_%H%M%S")

        json_file = f"output/acefuzz_{self.mode}_{timestamp}.json"
        txt_file = f"output/acefuzz_{self.mode}_{timestamp}.txt"

        # JSON
        with open(json_file, "w") as jf:
            json.dump(self.results, jf, indent=4)

        # TXT
        with open(txt_file, "w") as tf:
            for r in self.results:
                tf.write(self._format_txt(r) + "\n")

        return json_file, txt_file

    def _format_txt(self, r):
        return " | ".join(f"{k}={v}" for k, v in r.items())
