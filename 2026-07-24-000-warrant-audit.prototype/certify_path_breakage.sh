#!/bin/bash
# Re-runnable check certifying
# `claims.kb/link-checker-resolves-frontmatter-edges.md`.
#
# The claim: retracting a node by renaming it `NAME.retracted.md` makes
# every node that referenced it fail `llm.kb-validate-links` -- so RN's
# retraction propagation is enforced by a tool the fleet already runs,
# with no bespoke walker.
#
# The check: pick a referenced node, retract it, and assert that every
# referrer is named in the report. Restores the tree on any exit.
set -euo pipefail

realm="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
validate_links="${LLM_KB_VALIDATE_LINKS:-$HOME/repo/github.com/bukzor/bukzor-agent-skills/llm-kb/bin/llm.kb-validate-links}"
target="${1:-claims.kb/two-base-statuses-not-four.md}"

cd "$realm"
[[ -f $target ]] || { echo "no such node: $target" >&2; exit 2; }
[[ -x $validate_links ]] || { echo "no link checker: $validate_links" >&2; exit 2; }

# Referrers: any tracked node mentioning the target's basename. The
# checker resolves frontmatter fields unconditionally and body paths
# only in `./`-relative form, so this is the set it owes us -- and a
# miss means either a propagation gap or a body reference written in
# the unenforced bare form.
mapfile -t referrers < <(
    git ls-files -z -- '*.md' |
        xargs -0 grep -lF "$(basename "$target")" |
        grep -vxF "$target" | sort
)
((${#referrers[@]})) || { echo "$target has no referrers; pick another" >&2; exit 2; }

tombstone="${target%.md}.retracted.md"
trap 'mv -f "$tombstone" "$target" 2>/dev/null || true' EXIT
mv "$target" "$tombstone"

report="$("$validate_links" . 2>&1)" && {
    echo "FAIL: link checker passed with $target retracted" >&2
    exit 1
}

rc=0
for referrer in "${referrers[@]}"; do
    if grep -qF "$referrer" <<<"$report"; then
        echo "  ok      $referrer"
    else
        echo "  MISSING $referrer" >&2
        rc=1
    fi
done

((rc)) && { echo "FAIL: retraction did not propagate to every referrer" >&2; exit 1; }
echo "PASS: retracting $target surfaced all ${#referrers[@]} referrers"
