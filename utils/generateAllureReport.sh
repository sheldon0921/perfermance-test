#!/usr/bin/env bash
set -euo pipefail
export PATH="/opt/homebrew/opt/openjdk@21/bin:/opt/homebrew/bin:/usr/local/bin:$PATH"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=utils/common.sh
source "$SCRIPT_DIR/common.sh"

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

require_safe_clean_path "$ALLURE_REPORT_DIR" "Allure report directory"

safe_remove_path "$ALLURE_REPORT_DIR" "Allure report directory"
"$ALLURE_BIN" generate "$ALLURE_RESULTS_DIR" --clean -o "$ALLURE_REPORT_DIR"
echo "Allure report: $ALLURE_REPORT_DIR/index.html"
