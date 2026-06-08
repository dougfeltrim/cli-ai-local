# Gemini CLI Launcher
param(
  [string]$Model,
  [Parameter(ValueFromRemainingArguments = $true)]
  [string[]]$GeminiArgs
)

if (-not $Model) {
  if ($env:GEMINI_MODEL) {
    $Model = $env:GEMINI_MODEL
  } else {
    $Model = "gemini-2.0-flash"
  }
}

$ErrorActionPreference = "Stop"

Write-Host "=============================================" -ForegroundColor Cyan
Write-Host "         Local Gemini CLI Launcher" -ForegroundColor Cyan
Write-Host "=============================================" -ForegroundColor Cyan

if ($GeminiArgs -notcontains "--model" -and $GeminiArgs -notcontains "-m") {
  $GeminiArgs = @("--model", $Model) + $GeminiArgs
}

Write-Host "Launching gemini with args: $GeminiArgs" -ForegroundColor Gray

# Attempt to run gemini. Assumes 'gemini' is in the PATH.
& gemini @GeminiArgs
exit $LASTEXITCODE
