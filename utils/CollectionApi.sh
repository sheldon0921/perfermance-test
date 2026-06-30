#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=utils/common.sh
source "$SCRIPT_DIR/common.sh"

TARGET_PATH="${1:-PostmanScene}"
RESULT_DIR="${RESULT_DIR:-report/result}"
HTML_DIR="${HTML_DIR:-report/newman}"
NEWMAN_BIN="${NEWMAN_BIN:-node_modules/.bin/newman}"
COLLECTION_COUNT=0

validate_collection_file() {
  local collection="$1"

  if [ ! -f "$collection" ]; then
    echo "Collection file does not exist: $collection"
    exit 1
  fi

  case "$collection" in
    *.json) ;;
    *)
      echo "Collection file must be a .json file: $collection"
      exit 1
      ;;
  esac
}

clean_result_dir() {
  echo "Cleaning Newman report files: $RESULT_DIR"
  safe_recreate_dir "$RESULT_DIR" "result directory"

  echo "Cleaning Newman HTML files: $HTML_DIR"
  safe_recreate_dir "$HTML_DIR" "HTML directory"
}

if [ ! -x "$NEWMAN_BIN" ]; then
  echo "Newman is not installed. Run: npm install"
  exit 1
fi

if [ ! -e "$TARGET_PATH" ]; then
  echo "Target path does not exist: $TARGET_PATH"
  exit 1
fi

if [ -f "$TARGET_PATH" ]; then
  validate_collection_file "$TARGET_PATH"
fi

clean_result_dir

run_collection() {
  local collection="$1"
  local report_name

  validate_collection_file "$collection"
  COLLECTION_COUNT=$((COLLECTION_COUNT + 1))
  report_name="$(echo "$collection" | sed 's#^PostmanScene/##; s#[/ ]#_#g; s#\.json$##')"

  echo "Running collection: $collection"
  "$NEWMAN_BIN" run "$collection" \
    -r cli,junit \
    --reporter-junit-export "$RESULT_DIR/${report_name}.xml"
}

if [ -f "$TARGET_PATH" ]; then
  run_collection "$TARGET_PATH"
else
  while IFS= read -r collection; do
    [ -n "$collection" ] || continue
    run_collection "$collection"
  done < <(find "$TARGET_PATH" -type f -name '*.json' -print | sort)
fi

if [ "$COLLECTION_COUNT" -eq 0 ]; then
  echo "No Postman collection json files found in: $TARGET_PATH"
  exit 1
fi

echo "Newman collections completed: $COLLECTION_COUNT"
