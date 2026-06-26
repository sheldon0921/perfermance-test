#!/usr/bin/env bash
set -euo pipefail

JMETER_BIN="${JMETER_BIN:-jmeter}"
CASE_FILE="${1:-script/simulate/baidu_home.jmx}"
JTL_FILE="${JTL_FILE:-report/jtlResult.jtl}"
REPORT_DIR="${REPORT_DIR:-report/report}"
THREADS_COUNT="${ThreadsCount:-1}"
RAMP_UP="${RampUp:-1}"
DURATION="${time:-10}"
TARGET_DOMAIN="${TargetDomain:-www.baidu.com}"
TARGET_PROTOCOL="${TargetProtocol:-https}"
TARGET_PATH="${TargetPath:-/}"
THINK_TIME_MS="${ThinkTimeMs:-1000}"

is_safe_path() {
  local path="$1"
  [ -n "$path" ] && [ "$path" != "/" ] && [ "$path" != "." ]
}

validate_integer_at_least() {
  local name="$1"
  local value="$2"
  local minimum="$3"

  if ! [[ "$value" =~ ^[0-9]+$ ]] || [ "$value" -lt "$minimum" ]; then
    echo "$name must be an integer >= $minimum, got: $value"
    exit 1
  fi
}

validate_jmeter() {
  if ! command -v "$JMETER_BIN" >/dev/null 2>&1 && [ ! -x "$JMETER_BIN" ]; then
    echo "JMeter is not available: $JMETER_BIN"
    echo "Install it with: brew install jmeter"
    exit 1
  fi
}

validate_case_file() {
  if [ ! -f "$CASE_FILE" ]; then
    echo "JMeter case file does not exist: $CASE_FILE"
    exit 1
  fi

  case "$CASE_FILE" in
    *.jmx) ;;
    *)
      echo "JMeter case file must be a .jmx file: $CASE_FILE"
      exit 1
      ;;
  esac
}

clean_report_dir() {
  if ! is_safe_path "$REPORT_DIR"; then
    echo "Refusing to clean unsafe report directory: $REPORT_DIR"
    exit 1
  fi

  rm -rf "$REPORT_DIR"
  mkdir -p "$REPORT_DIR"
}

clean_jtl_file() {
  if ! is_safe_path "$JTL_FILE"; then
    echo "Refusing to clean unsafe JTL file: $JTL_FILE"
    exit 1
  fi

  rm -f "$JTL_FILE"
  mkdir -p "$(dirname "$JTL_FILE")"
}

validate_jmeter
validate_case_file
validate_integer_at_least "ThreadsCount" "$THREADS_COUNT" 1
validate_integer_at_least "RampUp" "$RAMP_UP" 0
validate_integer_at_least "time" "$DURATION" 1
validate_integer_at_least "ThinkTimeMs" "$THINK_TIME_MS" 0

echo "Cleaning JMeter report files..."
clean_jtl_file
clean_report_dir

echo "Running JMeter test: $CASE_FILE"
"$JMETER_BIN" -n \
  -t "$CASE_FILE" \
  -l "$JTL_FILE" \
  -e -o "$REPORT_DIR" \
  -JThreadsCount="$THREADS_COUNT" \
  -JRampUp="$RAMP_UP" \
  -Jtime="$DURATION" \
  -JTargetDomain="$TARGET_DOMAIN" \
  -JTargetProtocol="$TARGET_PROTOCOL" \
  -JTargetPath="$TARGET_PATH" \
  -JThinkTimeMs="$THINK_TIME_MS"

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
