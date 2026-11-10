"""Page-Hinkley drift detector."""


class PageHinkley:
    def __init__(self, delta: float = 0.0, threshold: float = 0.0):
        self.delta = delta
        self.threshold = threshold
        self._stream = None
        self._window = None
        self._sink = None

    def attach(self, stream, window: str = "24h"):
        self._stream = stream
        self._window = window
        return self

    def report(self, sink: str = "stdout"):
        self._sink = sink
        return self
