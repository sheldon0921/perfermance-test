#!/usr/bin/env bash
set -euo pipefail
export PATH="/opt/homebrew/opt/openjdk@21/bin:/opt/homebrew/bin:/usr/local/bin:$PATH"

ALLURE_BIN="${ALLURE_BIN:-node_modules/.bin/allure}"
ALLURE_RESULTS_DIR="${ALLURE_RESULTS_DIR:-report/allure-results}"
ALLURE_REPORT_DIR="${ALLURE_REPORT_DIR:-report/allure-report}"

if [ ! -x "$ALLURE_BIN" ]; then
  echo "Allure CLI is not installed. Run: npm install"
  exit 1
fi

if [ ! -d "$ALLURE_RESULTS_DIR" ]; then
  echo "Allure results directory does not exist: $ALLURE_RESULTS_DIR"
  exit 1
fi

if [ -z "$ALLURE_REPORT_DIR" ] || [ "$ALLURE_REPORT_DIR" = "/" ] || [ "$ALLURE_REPORT_DIR" = "." ]; then
  echo "Refusing to use unsafe Allure report directory: $ALLURE_REPORT_DIR"
  exit 1
fi

rm -rf "$ALLURE_REPORT_DIR"
"$ALLURE_BIN" generate "$ALLURE_RESULTS_DIR" --clean -o "$ALLURE_REPORT_DIR"
echo "Allure report: $ALLURE_REPORT_DIR/index.html"
