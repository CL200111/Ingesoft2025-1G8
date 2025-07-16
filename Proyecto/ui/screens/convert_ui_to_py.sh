#!/bin/bash

# Directory containing .ui files (default is current)
UI_DIR="."
OUTPUT_DIR="."

# Find all .ui files
for ui_file in "$UI_DIR"/*.ui; do
    # Extract filename without path and extension
    filename=$(basename -- "$ui_file")
    base="${filename%.ui}"

    # Construct output .py filename
    py_file="ui_${base}.py"

    echo "Converting $filename -> $py_file"
    pyuic5 "$ui_file" -o "$OUTPUT_DIR/$py_file"
done

echo "✅ All .ui files converted to .py"
