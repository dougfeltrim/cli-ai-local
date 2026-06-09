# Wrapper for LM Studio Launcher in PowerShell

param(
  [string]$Model,
  [Parameter(ValueFromRemainingArguments = $true)]
  [string[]]$ClaudeArgs
)

if (-not $Model) {
  if ($env:CLAUDE_MODEL) {
    $Model = $env:CLAUDE_MODEL
  } else {
    $Model = "gpt-oss:20b"
  }
}

Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "         Local LM Studio Launcher" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan

# Check if 'lms' exists
if (-not (Get-Command lms -ErrorAction SilentlyContinue)) {
  Write-Error "Erro: 'lms' (LM Studio CLI) não encontrado."
  exit 1
}

# Check if 'claude' exists
if (-not (Get-Command claude -ErrorAction SilentlyContinue)) {
  Write-Error "Erro: 'claude' CLI não encontrado."
  exit 1
}

# Unload previous models and load new one
Write-Host "Unloading previous models..." -ForegroundColor Gray
& lms unload -a

Write-Host "Loading model $Model with 38k context..." -ForegroundColor Gray
& lms load $Model --context-length 38000 --parallel 2 -y

# Set env variables for local host
$env:ANTHROPIC_BASE_URL = "http://localhost:1234"
$env:ANTHROPIC_AUTH_TOKEN = "lmstudio"

# Run Claude Code
Write-Host "Launching Claude Code..." -ForegroundColor Gray
& claude --model $Model --dangerously-skip-permissions @ClaudeArgs
exit $LASTEXITCODE
