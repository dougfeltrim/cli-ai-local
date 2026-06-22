#!/bin/bash
# Wrapper for Hermes Agent in Bash

MODEL=$1
shift # remove $1 from args
HERMES_ARGS=$@

if [ -z "$MODEL" ]; then
  if [ -n "$HERMES_MODEL" ] && [ "$HERMES_MODEL" != "none" ]; then
    MODEL=$HERMES_MODEL
  fi
fi

echo -e "\033[0;36m=============================================\033[0m"
echo -e "\033[0;36m      Local AI CLI Launcher (Hermes Agent)\033[0m"
echo -e "\033[0;36m=============================================\033[0m"
if [ -n "$MODEL" ]; then
  echo -e "\033[0;90mModel   : $MODEL\033[0m"
fi

if command -v hermes &> /dev/null; then
  if [ -n "$MODEL" ]; then
    echo -e "\033[0;90mRunning: hermes --model $MODEL $HERMES_ARGS\033[0m"
    hermes --model "$MODEL" "$@"
  else
    echo -e "\033[0;90mRunning: hermes $HERMES_ARGS\033[0m"
    hermes "$@"
  fi
  exit $?
else
  echo "Erro: 'hermes' CLI não está instalado ou não está no PATH."
  echo "Para instalar, execute: curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash"
  exit 1
fi
