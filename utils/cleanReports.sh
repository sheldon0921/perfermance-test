#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=utils/common.sh
source "$SCRIPT_DIR/common.sh"

MODE="${1:-local}"
RESULT_DIR="${RESULT_DIR:-report/result}"
HTML_DIR="${HTML_DIR:-report/newman}"
REPORT_DIR="${REPORT_DIR:-report/report}"
REPORT_HOME="${REPORT_HOME:-report/jenkins}"
ALLURE_RESULTS_DIR="${ALLURE_RESULTS_DIR:-report/allure-results}"
ALLURE_REPORT_DIR="${ALLURE_REPORT_DIR:-report/allure-report}"
JTL_FILE="${JTL_FILE:-report/jtlResult.jtl}"

clean_path() {
  local path="$1"
  local label="${2:-report path}"

  if [ -e "$path" ] || [ -L "$path" ]; then
    echo "Cleaning report path: $path"
  fi

  safe_remove_path "$path" "$label"
}

prepare_jmeter_outputs() {
  require_safe_clean_path "$REPORT_DIR" "JMeter report directory"
  require_safe_clean_path "$JTL_FILE" "JTL file"

  mkdir -p -- "$REPORT_DIR" "$(dirname "$JTL_FILE")"
  : > "$JTL_FILE"
}

clean_postman_outputs() {
  clean_path "$RESULT_DIR" "result directory"
  clean_path "$HTML_DIR" "HTML directory"
  clean_path "$REPORT_HOME" "report home"
  clean_path "$ALLURE_RESULTS_DIR" "Allure results directory"
  clean_path "$ALLURE_REPORT_DIR" "Allure report directory"
}

clean_jmeter_outputs() {
  clean_path "$REPORT_DIR" "JMeter report directory"
  clean_path "$REPORT_HOME" "report home"
  clean_path "$ALLURE_RESULTS_DIR" "Allure results directory"
  clean_path "$ALLURE_REPORT_DIR" "Allure report directory"
  clean_path "$JTL_FILE" "JTL file"
  prepare_jmeter_outputs
}

case "$MODE" in
  local|all)
    clean_path "$RESULT_DIR" "result directory"
    clean_path "$HTML_DIR" "HTML directory"
    clean_jmeter_outputs
    ;;
  postman|newman)
    clean_postman_outputs
    ;;
  jmeter)
    clean_jmeter_outputs
    ;;
  *)
    echo "Unknown clean reports mode: $MODE"
    echo "Usage: bash utils/cleanReports.sh [local|postman|jmeter]"
    exit 1
    ;;
esac
