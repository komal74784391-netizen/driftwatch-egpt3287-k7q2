from driftwatch.streams import FeatureStream
from driftwatch.detectors import PageHinkley

stream = FeatureStream("redis://localhost:6379")
detector = PageHinkley(delta=0.01, threshold=0.4).attach(stream, window="6h")
print("replay ready")
