#!/usr/bin/env bash

is_safe_clean_path() {
  local path="$1"

  [ -n "$path" ] || return 1

  # Report scripts only clean workspace-relative output paths.
  case "$path" in
    -*|/*|.|..|*/../*|../*|*/..)
      return 1
      ;;
  esac

  return 0
}

require_safe_clean_path() {
  local path="$1"
  local label="${2:-path}"

  if ! is_safe_clean_path "$path"; then
    echo "Refusing to use unsafe $label: $path"
    exit 1
  fi
}

safe_recreate_dir() {
  local path="$1"
  local label="${2:-directory}"

  require_safe_clean_path "$path" "$label"
  rm -rf -- "$path"
  mkdir -p -- "$path"
}

safe_remove_path() {
  local path="$1"
  local label="${2:-path}"

  require_safe_clean_path "$path" "$label"
  rm -rf -- "$path"
}

safe_prepare_file() {
  local path="$1"
  local label="${2:-file}"

  require_safe_clean_path "$path" "$label"
  rm -f -- "$path"
  mkdir -p -- "$(dirname "$path")"
}

require_boolean_flag() {
  local value="$1"
  local name="$2"

  case "$value" in
    0|1) ;;
    *)
      echo "$name must be 0 or 1, got: $value"
      exit 1
      ;;
  esac
}

require_valid_test_type() {
  local value="$1"
  local name="${2:-TEST_TYPE}"

  case "$value" in
    ''|unknown|local|postman|jmeter) ;;
    *)
      echo "$name must be one of: postman, jmeter, local, unknown; got: $value"
      exit 1
      ;;
  esac
}
