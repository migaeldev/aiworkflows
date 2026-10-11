#!/usr/bin/env sh
# Fetch the aiworkspace harness with a shallow clone and run its installer, so a target repo
# never needs a manual checkout of the harness.
#
#   curl -fsSL <raw-url-of-this-script> | sh -s -- <repo-url> [target-repo] [install.py options]
#
# repo-url can be omitted (and dropped from argv entirely) if AIWORKSPACE_REPO_URL is set:
#   AIWORKSPACE_REPO_URL=<repo-url> curl -fsSL <raw-url-of-this-script> | sh -s -- [target-repo] [options]
#
# target-repo defaults to the current directory. The clone is removed when the script exits,
# whether or not the install succeeds.

set -eu

usage() {
    echo "usage: $0 [<repo-url>] [target-repo] [install.py options]" >&2
    echo "       repo-url may be omitted if \$AIWORKSPACE_REPO_URL is set" >&2
    echo "       target-repo defaults to the current directory" >&2
    exit 2
}

if [ -n "${AIWORKSPACE_REPO_URL:-}" ]; then
    REPO_URL="$AIWORKSPACE_REPO_URL"
else
    [ "$#" -ge 1 ] || usage
    REPO_URL="$1"
    shift
fi

command -v git >/dev/null 2>&1 || { echo "error: git is required" >&2; exit 1; }
PYTHON=python3
command -v "$PYTHON" >/dev/null 2>&1 || PYTHON=python
command -v "$PYTHON" >/dev/null 2>&1 || { echo "error: python (3.8+) is required" >&2; exit 1; }

TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

git clone --depth 1 --quiet "$REPO_URL" "$TMP/harness"
"$PYTHON" "$TMP/harness/tools/install.py" "$@"
