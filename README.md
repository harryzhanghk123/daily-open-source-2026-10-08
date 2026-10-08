# Daily Open Source 2026-10-08

A tiny, dependency-free command-line utility that turns a list of tasks into a prioritized plan.

## Usage

Requires Python 3.10+.

```bash
python -m planmaker "ship release" "write tests" "review pull request"
```

Tasks are ranked by urgency markers (`!`), then by length, with stable ordering for ties. This makes it useful in shell scripts and easy to inspect or extend.

## Development

Run the tests with:

```bash
python -m unittest discover -s tests -v
```

## License

MIT. See [LICENSE](LICENSE).
