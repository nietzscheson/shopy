#!/bin/bash

# ANSI Color Codes
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Ensure the repository is up-to-date
git fetch

# Get the current branch name
current_branch=$(git rev-parse --abbrev-ref HEAD)

# If you're not on the main branch, check for commits
if [[ "$current_branch" != "main" && "$current_branch" != "master" ]]; then
    # Get the count of unique commits the current branch has compared to origin/main
    commit_count=$(git rev-list --count $current_branch ^origin/main)

    if [ "$commit_count" -gt 1 ]; then
        echo -e "${RED}Error: $current_branch has more than 1 commit over origin/main. Please squash or rebase your commits.${NC}"
        exit 1
    fi
fi

echo -e "${GREEN}Pre-commit check passed.${NC}"
