#!/bin/bash

# Codex Launcher for Unix
MODEL="${CODEX_MODEL:-gpt-oss:20b}"

echo "============================================="
echo "         Local Codex Launcher"
echo "============================================="

if command -v codex &> /dev/null; then
    codex --model "$MODEL" "$@"
else
    echo "Erro: 'codex' CLI não está instalado ou não está no PATH."
    exit 1
fi
