#!/usr/bin/env python3
"""Compatibility placeholder for the retired pytest entrypoint.

This repository is maintained as a Newman/JMeter test project. Use the npm
scripts documented in README.md to run interface and performance tests.
"""

import sys

MESSAGE = "This project no longer uses main.py. Run `npm run postman` or `npm run jmeter`."


if __name__ == "__main__":
    print(MESSAGE, file=sys.stderr)
    sys.exit(1)
