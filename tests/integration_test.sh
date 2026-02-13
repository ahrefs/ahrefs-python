#!/usr/bin/env bash
# Standalone integration test: fresh venv -> install -> test against live API
#
# Usage: ./tests/integration_test.sh
# Requires: .env file with AHREFS_API_KEY=<key> (or AHREFS_API_KEY already exported)
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
VENV_DIR="$PROJECT_DIR/.venv-integration-test"

cleanup() {
    echo ""
    echo "Cleaning up venv at $VENV_DIR ..."
    rm -rf "$VENV_DIR"
}
trap cleanup EXIT

# Load .env if present (only AHREFS_API_KEY)
if [[ -z "${AHREFS_API_KEY:-}" ]]; then
    for envfile in "$PROJECT_DIR/.env" "$SCRIPT_DIR/.env"; do
        if [[ -f "$envfile" ]]; then
            value=$(grep -E '^AHREFS_API_KEY=' "$envfile" | head -1 | cut -d= -f2-)
            if [[ -n "$value" ]]; then
                export AHREFS_API_KEY="$value"
                echo "Loaded AHREFS_API_KEY from $envfile"
                break
            fi
        fi
    done
fi

if [[ -z "${AHREFS_API_KEY:-}" ]]; then
    echo "ERROR: AHREFS_API_KEY not found."
    echo "Set it via environment or create a .env file with AHREFS_API_KEY=<key>"
    exit 1
fi

echo "Creating fresh venv at $VENV_DIR ..."
python3 -m venv "$VENV_DIR"

echo "Installing ahrefs-python from source ..."
"$VENV_DIR/bin/pip" install --quiet "$PROJECT_DIR"

echo "Running integration tests ..."
echo ""
"$VENV_DIR/bin/python" "$SCRIPT_DIR/integration_test.py"
