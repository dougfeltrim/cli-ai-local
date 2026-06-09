# Wrapper for Codex Launcher in PowerShell

param(
  [string]$Model,
  [Parameter(ValueFromRemainingArguments = $true)]
  [string[]]$CodexArgs
)

if (-not $Model) {
  if ($env:CODEX_MODEL) {
    $Model = $env:CODEX_MODEL
  } else {
    $Model = "gpt-oss:20b"
  }
}

Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "         Local Codex Launcher" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan

if (Get-Command codex -ErrorAction SilentlyContinue) {
  Write-Host "Running: codex --model $Model $CodexArgs" -ForegroundColor Gray
  & codex --model $Model @CodexArgs
} else {
  Write-Error "Erro: 'codex' CLI não está instalado ou não está no PATH."
  exit 1
}
exit $LASTEXITCODE
