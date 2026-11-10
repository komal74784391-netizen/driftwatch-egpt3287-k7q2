from driftwatch.detectors import PageHinkley


def test_attach():
    detector = PageHinkley(delta=0.01, threshold=0.4)
    assert detector.attach(object()).threshold == 0.4
