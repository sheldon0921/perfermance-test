#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=utils/common.sh
source "$SCRIPT_DIR/common.sh"

POSTMAN_COLLECTION="${POSTMAN_COLLECTION:-PostmanScene/BaiduDemo/BaiduHome.json}"
JMETER_CASE_FILE="${JMETER_CASE_FILE:-script/simulate/baidu_home.jmx}"
RUN_NPM_AUDIT="${RUN_NPM_AUDIT:-1}"
RUN_SAFETY_CHECK="${RUN_SAFETY_CHECK:-1}"
RUN_STATIC_CHECK="${RUN_STATIC_CHECK:-1}"

require_boolean_flag "$RUN_NPM_AUDIT" "RUN_NPM_AUDIT"
require_boolean_flag "$RUN_SAFETY_CHECK" "RUN_SAFETY_CHECK"
require_boolean_flag "$RUN_STATIC_CHECK" "RUN_STATIC_CHECK"

step() {
  printf '\n==> %s\n' "$1"
}

step "Verify Node dependencies"
if [ ! -d node_modules ]; then
  npm ci
fi

if [ "$RUN_NPM_AUDIT" = "1" ]; then
  npm audit
fi

if [ "$RUN_STATIC_CHECK" = "1" ]; then
  step "Verify shell scripts and cleanup usage"
  bash utils/verifyStatic.sh
fi

if [ "$RUN_SAFETY_CHECK" = "1" ]; then
  step "Verify cleanup safety guards"
  bash utils/verifySafety.sh
fi

step "Run Newman collection: $POSTMAN_COLLECTION"
bash utils/CollectionApi.sh "$POSTMAN_COLLECTION"

step "Run JMeter case: $JMETER_CASE_FILE"
bash utils/runJmeter.sh "$JMETER_CASE_FILE"

step "Generate Allure report"
TEST_TYPE=local bash utils/generateAllureResults.sh
bash utils/generateAllureReport.sh

step "Generate local report index"
TEST_TYPE=local bash utils/buildReportIndex.sh

printf '\nLocal verification completed. Open report/jenkins/index.html for the report index.\n'
