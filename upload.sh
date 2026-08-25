#!/bin/bash
echo "🚀 Starting Automated GitHub Upload..."

# Check if git is initialized
if [ ! -d ".git" ]; then
    git init
    echo "Initialized empty Git repository."
fi

# Add all files
git add .

# Commit with prompt message or default
git commit -m "chore: automated update and proof of work sync"

# Push to main
git branch -M main
git push -u origin main

echo "✅ Successfully uploaded project to GitHub!"