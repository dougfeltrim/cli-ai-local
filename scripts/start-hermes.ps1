# Wrapper for Hermes Agent in PowerShell

param(
  [string]$Model,
  [Parameter(ValueFromRemainingArguments = $true)]
  [string[]]$HermesArgs
)

if (-not $Model) {
  if ($env:HERMES_MODEL -and $env:HERMES_MODEL -ne "none") {
    $Model = $env:HERMES_MODEL
  }
}

Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "      Local AI CLI Launcher (Hermes Agent)" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan
if ($Model) {
  Write-Host "Model   : $Model" -ForegroundColor Gray
}

# Check if 'hermes' CLI exists in the system
if (Get-Command hermes -ErrorAction SilentlyContinue) {
  $cmdArgs = @()
  if ($Model) {
    $cmdArgs += "--model"
    $cmdArgs += $Model
  }
  $cmdArgs += $HermesArgs
  
  Write-Host "Running: hermes $cmdArgs" -ForegroundColor Gray
  & hermes @cmdArgs
} else {
  Write-Error "Erro: 'hermes' CLI não está instalado ou não está no PATH."
  Write-Host "Para instalar, execute: iex (irm https://hermes-agent.nousresearch.com/install.ps1)" -ForegroundColor Yellow
  exit 1
}
exit $LASTEXITCODE
