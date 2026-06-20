#!/usr/bin/env bash
set -euo pipefail

JMETER_BIN="${JMETER_BIN:-jmeter}"
JTL_FILE="${JTL_FILE:-report/jtlResult.jtl}"
REPORT_DIR="${REPORT_DIR:-report/report}"

clean_report_dir() {
  if [ -z "$REPORT_DIR" ] || [ "$REPORT_DIR" = "/" ] || [ "$REPORT_DIR" = "." ]; then
    echo "Refusing to clean unsafe report directory: $REPORT_DIR"
    exit 1
  fi

  echo "Cleaning JMeter HTML report files: $REPORT_DIR"
  rm -rf "$REPORT_DIR"
  mkdir -p "$REPORT_DIR"
}

if [ ! -s "$JTL_FILE" ]; then
  echo "JMeter result file does not exist or is empty: $JTL_FILE"
  exit 1
fi

clean_report_dir

"$JMETER_BIN" -g "$JTL_FILE" -e -o "$REPORT_DIR"

echo "JMeter report: $REPORT_DIR/index.html"
