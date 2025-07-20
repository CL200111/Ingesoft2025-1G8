#!/bin/bash

# === Configuration ===
VENV_DIR=".venv"
PROJECT_DIR="."  # Change if your source is in a subfolder
LOG_DIR="logs"

# === Prepare log directory ===
mkdir -p "$LOG_DIR"

# === Step 3: Run linters ===
source "$VENV_DIR/bin/activate"

echo "🔍 Running ruff (style and lint check)..."
ruff check "$PROJECT_DIR" > "$LOG_DIR/ruff.log" 2>&1

echo "🔎 Running mypy (type checker)..."
mypy "$PROJECT_DIR" > "$LOG_DIR/mypy.log" 2>&1

echo "🛡️ Running bandit (security scan)..."
bandit -r "$PROJECT_DIR" > "$LOG_DIR/bandit.log" 2>&1

echo "🧪 Running tests with coverage..."
coverage run -m unittest discover "$PROJECT_DIR" > "$LOG_DIR/coverage_run.log" 2>&1
coverage report > "$LOG_DIR/coverage_report.log" 2>&1

echo "✅ All checks complete! Logs saved in $LOG_DIR/"
