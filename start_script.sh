#!/bin/bash

# Check if a filename argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: docker run my-python-app <filename>"
    exit 1
fi

# Run the Python script provided as an argument
python "$@"
