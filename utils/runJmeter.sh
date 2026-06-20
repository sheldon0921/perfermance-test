#!/usr/bin/env bash
set -euo pipefail

JMETER_BIN="${JMETER_BIN:-jmeter}"
CASE_FILE="${1:-script/simulate/baidu_home.jmx}"
JTL_FILE="${JTL_FILE:-report/jtlResult.jtl}"
REPORT_DIR="${REPORT_DIR:-report/report}"
THREADS_COUNT="${ThreadsCount:-10}"
RAMP_UP="${RampUp:-10}"
DURATION="${time:-60}"

validate_integer_at_least() {
  local name="$1"
  local value="$2"
  local minimum="$3"

  if ! [[ "$value" =~ ^[0-9]+$ ]] || [ "$value" -lt "$minimum" ]; then
    echo "$name must be an integer >= $minimum, got: $value"
    exit 1
  fi
}

clean_report_dir() {
  if [ -z "$REPORT_DIR" ] || [ "$REPORT_DIR" = "/" ] || [ "$REPORT_DIR" = "." ]; then
    echo "Refusing to clean unsafe report directory: $REPORT_DIR"
    exit 1
  fi

  rm -rf "$REPORT_DIR"
  mkdir -p "$REPORT_DIR"
}

clean_jtl_file() {
  if [ -z "$JTL_FILE" ] || [ "$JTL_FILE" = "/" ] || [ "$JTL_FILE" = "." ]; then
    echo "Refusing to clean unsafe JTL file: $JTL_FILE"
    exit 1
  fi

  rm -f "$JTL_FILE"
  mkdir -p "$(dirname "$JTL_FILE")"
}

echo "Cleaning JMeter report files..."
validate_integer_at_least "ThreadsCount" "$THREADS_COUNT" 1
validate_integer_at_least "RampUp" "$RAMP_UP" 0
validate_integer_at_least "time" "$DURATION" 1
clean_jtl_file
clean_report_dir

echo "Running JMeter test: $CASE_FILE"
"$JMETER_BIN" -n \
  -t "$CASE_FILE" \
  -l "$JTL_FILE" \
  -e -o "$REPORT_DIR" \
  -JThreadsCount="$THREADS_COUNT" \
  -JRampUp="$RAMP_UP" \
  -Jtime="$DURATION"

if [ ! -s "$JTL_FILE" ]; then
  echo "JMeter result file was not generated: $JTL_FILE"
  exit 1
fi

if [ "$(wc -l < "$JTL_FILE")" -le 1 ]; then
  echo "JMeter result file has no samples: $JTL_FILE"
  exit 1
fi

if [ ! -f "$REPORT_DIR/index.html" ]; then
  echo "JMeter HTML report was not generated: $REPORT_DIR/index.html"
  exit 1
fi

echo "JMeter report: $REPORT_DIR/index.html"
