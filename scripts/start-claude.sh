#!/bin/bash

# Verificar se comandos básicos existem
check_command() {
    if ! command -v "$1" &> /dev/null; then
        echo "Aviso: Comando '$1' não encontrado. Certifique-se de que está instalado."
    fi
}

echo "============================================="
echo "      Local AI CLI Launcher (Unix Check)"
echo "============================================="

# Detectar se estamos rodando dentro do diretório scripts ou via launcher
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

# Verificar dependências
check_command "claude"
check_command "python3"

DEFAULT_URL="http://localhost:1234"
MODEL="${CLAUDE_MODEL:-gpt-oss:20b}"

export ANTHROPIC_BASE_URL="${ANTHROPIC_BASE_URL:-$DEFAULT_URL}"
export ANTHROPIC_AUTH_TOKEN="${ANTHROPIC_AUTH_TOKEN:-lmstudio}"

echo "Base URL: $ANTHROPIC_BASE_URL"
echo "Model   : $MODEL"

# Executar
if command -v claude &> /dev/null; then
    claude --model "$MODEL" --dangerously-skip-permissions "$@"
else
    echo "Erro: 'claude' CLI não está instalado ou não está no PATH."
    exit 1
fi
