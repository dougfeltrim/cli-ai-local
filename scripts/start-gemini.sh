#!/bin/bash

# Gemini CLI Launcher for Unix
MODEL="${GEMINI_MODEL:-gemini-2.0-flash}"
ARGS=("$@")

echo "============================================="
echo "         Local Gemini CLI Launcher"
echo "============================================="

# Check if --model or -m is in args
HAS_MODEL=false
for arg in "${ARGS[@]}"; do
    if [[ "$arg" == "--model" || "$arg" == "-m" ]]; then
        HAS_MODEL=true
        break
    fi
done

if [ "$HAS_MODEL" = false ]; then
    ARGS=("--model" "$MODEL" "${ARGS[@]}")
fi

echo "Launching gemini with args: ${ARGS[@]}"

# Attempt to run gemini. Assumes 'gemini' is in the PATH.
gemini "${ARGS[@]}"
exit $?
