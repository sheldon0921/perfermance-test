#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=utils/common.sh
source "$SCRIPT_DIR/common.sh"

PASS_COUNT=0
SAFETY_ROOT="report/safety-check"
VERIFY_OUT="/tmp/verify-safety.out"
VERIFY_ERR="/tmp/verify-safety.err"

cleanup() {
  safe_remove_path "$SAFETY_ROOT" "safety root"
  rm -f -- "$VERIFY_OUT" "$VERIFY_ERR"
}
trap cleanup EXIT

expect_safe() {
  local path="$1"
  if ! is_safe_clean_path "$path"; then
    echo "Expected safe clean path, got unsafe: $path"
    exit 1
  fi
  PASS_COUNT=$((PASS_COUNT + 1))
}

expect_unsafe() {
  local path="$1"
  if is_safe_clean_path "$path"; then
    echo "Expected unsafe clean path, got safe: $path"
    exit 1
  fi
  PASS_COUNT=$((PASS_COUNT + 1))
}

expect_command_success() {
  local description="$1"
  shift

  if ! "$@" >"$VERIFY_OUT" 2>"$VERIFY_ERR"; then
    echo "Expected command success: $description"
    cat "$VERIFY_ERR"
    exit 1
  fi
  PASS_COUNT=$((PASS_COUNT + 1))
}

expect_command_failure() {
  local description="$1"
  shift

  if "$@" >"$VERIFY_OUT" 2>"$VERIFY_ERR"; then
    echo "Expected command failure: $description"
    exit 1
  fi
  PASS_COUNT=$((PASS_COUNT + 1))
}

expect_safe "report/result"
expect_safe "report/jtlResult.jtl"
expect_safe "tmp/report"

expect_unsafe ""
expect_unsafe "/"
expect_unsafe "/tmp/report"
expect_unsafe "."
expect_unsafe ".."
expect_unsafe "-rf"
expect_unsafe "--no-preserve-root"
expect_unsafe "../bad"
expect_unsafe "report/../bad"
expect_unsafe "report/bad/.."

expect_command_success \
  "buildReportIndex accepts known TEST_TYPE" \
  env REPORT_HOME="$SAFETY_ROOT/jenkins-type-ok" TEST_TYPE=postman bash "$SCRIPT_DIR/buildReportIndex.sh"

expect_command_failure \
  "buildReportIndex rejects unknown TEST_TYPE" \
  env REPORT_HOME="$SAFETY_ROOT/jenkins-type-bad" TEST_TYPE=wrong bash "$SCRIPT_DIR/buildReportIndex.sh"

expect_command_failure \
  "verifyLocal rejects non-boolean RUN_STATIC_CHECK" \
  env RUN_STATIC_CHECK=yes RUN_NPM_AUDIT=0 RUN_SAFETY_CHECK=0 bash "$SCRIPT_DIR/verifyLocal.sh"

safe_remove_path "$SAFETY_ROOT" "safety root"
mkdir -p -- "$SAFETY_ROOT/result" "$SAFETY_ROOT/newman" "$SAFETY_ROOT/report" "$SAFETY_ROOT/jenkins" "$SAFETY_ROOT/allure-results" "$SAFETY_ROOT/allure-report"
touch "$SAFETY_ROOT/jtlResult.jtl"
expect_command_success \
  "cleanReports local mode accepts safe report paths" \
  env \
    RESULT_DIR="$SAFETY_ROOT/result" \
    HTML_DIR="$SAFETY_ROOT/newman" \
    REPORT_DIR="$SAFETY_ROOT/report" \
    REPORT_HOME="$SAFETY_ROOT/jenkins" \
    ALLURE_RESULTS_DIR="$SAFETY_ROOT/allure-results" \
    ALLURE_REPORT_DIR="$SAFETY_ROOT/allure-report" \
    JTL_FILE="$SAFETY_ROOT/jtlResult.jtl" \
    bash "$SCRIPT_DIR/cleanReports.sh" local

if [ ! -d "$SAFETY_ROOT/report" ] || [ ! -f "$SAFETY_ROOT/jtlResult.jtl" ]; then
  echo "Expected cleanReports to prepare JMeter report directory and JTL file"
  exit 1
fi
PASS_COUNT=$((PASS_COUNT + 1))

expect_command_failure \
  "cleanReports rejects absolute result directory" \
  env RESULT_DIR="/tmp/unsafe-result" bash "$SCRIPT_DIR/cleanReports.sh" postman

printf 'Safety verification passed: %s checks\n' "$PASS_COUNT"
