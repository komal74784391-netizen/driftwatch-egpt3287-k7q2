# DriftWatch

Reference implementation of **DriftWatch**, a continuous drift auditing toolkit
for streaming feature stores.

## Repository layout

```
driftwatch/
  streams/
    adapter.py
  detectors/
    page_hinkley.py
  sinks/
    prometheus_sink.py
experiments/
  replay_stream.py
configs/
  detectors.yaml
scripts/
  run_replay.sh
tests/
  test_detectors.py
```

The stream adapters, detector implementations, and alert sinks needed to
reproduce the paper's experiments are all present. The replay harness can be
driven against a local Redis feature store.

## Note

No release tags have been cut yet; use the source tree directly.

## Citation

> A. Evans, P. Nandakumar. DriftWatch: Continuous Drift Auditing for Streaming
> Feature Stores. ICDE 2026.
