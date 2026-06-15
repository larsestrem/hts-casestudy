#!/usr/bin/env bash
# Regenerate the flat build, commit source + build, and push to main.
# Cloudflare Pages (connected to this repo, output dir = build/) deploys automatically.
# Usage: ./deploy.sh "short message describing what changed"
set -euo pipefail
cd "$(dirname "$0")"
MSG="${1:-Update HTS case study}"

python3 flatten.py

git add -A
if git diff --cached --quiet; then
  echo "No changes to deploy."
  exit 0
fi
git commit -m "$MSG"
# Deploy current work to main regardless of local branch name.
git push origin HEAD:main
echo "Pushed to main. Cloudflare Pages will build and deploy ./build automatically."
