"""Adapter for reading feature records from a streaming store."""


class FeatureStream:
    def __init__(self, uri: str):
        self.uri = uri

    def records(self):
        yield {"user": "u-1", "score": 0.73}
