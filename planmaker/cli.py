"""Prioritize tasks from the command line."""
from __future__ import annotations

import argparse


def prioritize(tasks: list[str]) -> list[str]:
    """Return tasks ordered by urgency marker, then concise tasks first."""
    return sorted(enumerate(tasks), key=lambda item: (0 if "!" in item[1] else 1, len(item[1]), item[0]))


def main() -> None:
    parser = argparse.ArgumentParser(description="Turn tasks into a prioritized plan")
    parser.add_argument("tasks", nargs="+")
    args = parser.parse_args()
    for number, (_, task) in enumerate(prioritize(args.tasks), 1):
        print(f"{number}. {task}")


if __name__ == "__main__":
    main()
