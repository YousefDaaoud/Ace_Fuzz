from collections import Counter

class SmartFilter:
    def __init__(self):
        self.status_common = set()
        self.length_common = set()
        self.word_common = set()

    def learn(self, responses):
        statuses = [r.status_code for r in responses]
        lengths = [len(r.text) for r in responses]
        words = [len(r.text.split()) for r in responses]

        self.status_common = self._top_values(statuses)
        self.length_common = self._top_values(lengths)
        self.word_common = self._top_values(words)

    def _top_values(self, data, threshold=0.6):
        c = Counter(data)
        total = sum(c.values())

        return {
            k for k, v in c.items()
            if (v / total) >= threshold
        }

    def is_noise(self, response):
        if response.status_code in self.status_common:
            if len(response.text) in self.length_common:
                if len(response.text.split()) in self.word_common:
                    return True
        return False
