# Wrapper for Claude Launcher in PowerShell

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

$defaultUrl = "http://localhost:1234"
if (-not $env:ANTHROPIC_BASE_URL) {
  $env:ANTHROPIC_BASE_URL = $defaultUrl
}
if (-not $env:ANTHROPIC_AUTH_TOKEN) {
  $env:ANTHROPIC_AUTH_TOKEN = "lmstudio"
}

Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "      Local AI CLI Launcher (Claude Code)" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "Base URL: $env:ANTHROPIC_BASE_URL" -ForegroundColor Gray
Write-Host "Model   : $Model" -ForegroundColor Gray

# Check if 'claude' CLI exists in the system
if (Get-Command claude -ErrorAction SilentlyContinue) {
  Write-Host "Running: claude --model $Model --dangerously-skip-permissions $ClaudeArgs" -ForegroundColor Gray
  & claude --model $Model --dangerously-skip-permissions @ClaudeArgs
} else {
  Write-Error "Erro: 'claude' CLI não está instalado ou não está no PATH."
  exit 1
}
exit $LASTEXITCODE
