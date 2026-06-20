#!/usr/bin/env bash
set -euo pipefail

TARGET_PATH="${1:-PostmanScene}"
RESULT_DIR="${RESULT_DIR:-report/result}"
HTML_DIR="${HTML_DIR:-report/newman}"
NEWMAN_BIN="${NEWMAN_BIN:-node_modules/.bin/newman}"

clean_result_dir() {
  if [ -z "$RESULT_DIR" ] || [ "$RESULT_DIR" = "/" ] || [ "$RESULT_DIR" = "." ]; then
    echo "Refusing to clean unsafe result directory: $RESULT_DIR"
    exit 1
  fi

  echo "Cleaning Newman report files: $RESULT_DIR"
  rm -rf "$RESULT_DIR"
  mkdir -p "$RESULT_DIR"

  if [ -z "$HTML_DIR" ] || [ "$HTML_DIR" = "/" ] || [ "$HTML_DIR" = "." ]; then
    echo "Refusing to clean unsafe HTML directory: $HTML_DIR"
    exit 1
  fi

  echo "Cleaning Newman HTML files: $HTML_DIR"
  rm -rf "$HTML_DIR"
  mkdir -p "$HTML_DIR"
}

if [ ! -x "$NEWMAN_BIN" ]; then
  echo "Newman is not installed. Run: npm install"
  exit 1
fi

if [ ! -e "$TARGET_PATH" ]; then
  echo "Target path does not exist: $TARGET_PATH"
  exit 1
fi

clean_result_dir

run_collection() {
  local collection="$1"
  local report_name
  report_name="$(echo "$collection" | sed 's#^PostmanScene/##; s#[/ ]#_#g; s#\.json$##')"

  echo "Running collection: $collection"
  "$NEWMAN_BIN" run "$collection" \
    -r cli,junit \
    --reporter-junit-export "$RESULT_DIR/${report_name}.xml"
}

if [ -f "$TARGET_PATH" ]; then
  run_collection "$TARGET_PATH"
else
  while IFS= read -r -d '' collection; do
    run_collection "$collection"
  done < <(find "$TARGET_PATH" -type f -name '*.json' -print0)
fi
