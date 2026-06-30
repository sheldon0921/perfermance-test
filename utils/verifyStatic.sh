#!/usr/bin/env bash
set -euo pipefail

FORBIDDEN_RM_TARGETS=(
  Jenkinsfile
  JenkinsfileForLocal
  JenkinsfileForNewman
  utils/CollectionApi.sh
  utils/runJmeter.sh
  utils/generateJmeterReport.sh
  utils/generateAllureResults.sh
  utils/generateAllureReport.sh
  utils/buildReportIndex.sh
  utils/cleanReports.sh
)

printf 'Checking shell syntax...\n'
bash -n utils/*.sh

printf 'Checking direct destructive cleanup usage...\n'
if rg -n 'rm -rf' "${FORBIDDEN_RM_TARGETS[@]}"; then
  echo "Direct rm -rf is not allowed outside utils/common.sh; use safe cleanup helpers instead."
  exit 1
fi

printf 'Static verification passed\n'
