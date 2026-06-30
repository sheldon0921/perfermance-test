#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=utils/common.sh
source "$SCRIPT_DIR/common.sh"

JMETER_BIN="${JMETER_BIN:-jmeter}"
JTL_FILE="${JTL_FILE:-report/jtlResult.jtl}"
REPORT_DIR="${REPORT_DIR:-report/report}"

clean_report_dir() {
  echo "Cleaning JMeter HTML report files: $REPORT_DIR"
  safe_recreate_dir "$REPORT_DIR" "report directory"
}

if ! command -v "$JMETER_BIN" >/dev/null 2>&1 && [ ! -x "$JMETER_BIN" ]; then
  echo "JMeter is not available: $JMETER_BIN"
  echo "Install it with: brew install jmeter"
  exit 1
fi

if [ ! -s "$JTL_FILE" ]; then
  echo "JMeter result file does not exist or is empty: $JTL_FILE"
  exit 1
fi

if ! head -n 1 "$JTL_FILE" | grep -q 'timeStamp'; then
  echo "JMeter result file does not look like a CSV JTL file: $JTL_FILE"
  exit 1
fi

clean_report_dir

"$JMETER_BIN" -g "$JTL_FILE" -e -o "$REPORT_DIR"

echo "JMeter report: $REPORT_DIR/index.html"
