#!/bin/bash

# LM Studio Launcher for Unix
MODEL="${CLAUDE_MODEL:-gpt-oss:20b}"

echo "============================================="
echo "         Local LM Studio Launcher"
echo "============================================="

if ! command -v lms &> /dev/null; then
    echo "Erro: 'lms' (LM Studio CLI) não encontrado."
    exit 1
fi

if ! command -v claude &> /dev/null; then
    echo "Erro: 'claude' CLI não encontrado."
    exit 1
fi

# Unload e Load
lms unload -a
lms load "$MODEL" --context-length 38000 --parallel 2 -y

# Env vars
export ANTHROPIC_BASE_URL="http://localhost:1234"
export ANTHROPIC_AUTH_TOKEN="lmstudio"

claude --model "$MODEL" --dangerously-skip-permissions "$@"
exit $?
