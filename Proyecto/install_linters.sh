#!/bin/bash

# === Configuration ===
VENV_DIR=".venv"
PROJECT_DIR="."  # Change this if your code lives in a subfolder
PYTHON_BIN="python3"

# === Step 1: Create virtual environment ===
echo "🔧 Creating virtual environment in $VENV_DIR..."
$PYTHON_BIN -m venv "$VENV_DIR"
source "$VENV_DIR/bin/activate"

# === Step 2: Upgrade pip and install tools ===
echo "📦 Installing linters and analysis tools..."
pip install --upgrade pip
pip install ruff mypy bandit coverage

