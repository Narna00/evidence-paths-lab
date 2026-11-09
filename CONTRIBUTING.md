# Contributing

Contributions should include a clear research or engineering objective, the affected model assumptions and a reproducible example. Changes to decision semantics require a regression test. Experimental contributions should record software versions, configurations, seeds, exclusions and protocol deviations, including negative and inconclusive outcomes.

Run the test suite with Python 3.12 or later:

```sh
python -m unittest discover -v
```

Documentation changes should use research terminology consistently, cite primary sources and distinguish measured results from proposed methods. Mathematical statements should identify their assumptions; empirical comparisons should identify their experimental unit and applicable baselines.

Examples and submitted artifacts must use synthetic or appropriately licensed data. Client records, credentials, private target inventories and personal data are unsuitable for public issues or pull requests. Security reports follow [SECURITY.md](SECURITY.md).
