import difflib

class Similarity:
    def __init__(self, threshold=0.95):
        self.threshold = threshold

    def is_similar(self, base_text, new_text):
        ratio = difflib.SequenceMatcher(
            None, base_text, new_text
        ).ratio()

        return ratio >= self.threshold, ratio
