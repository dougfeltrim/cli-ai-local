# Wrapper for LM Studio Launcher
$rootPath = (Get-Item $PSScriptRoot).Parent.FullName
$scriptPath = Join-Path $rootPath "scripts\start-lmstudio-local.ps1"

if (-not (Test-Path $scriptPath)) {
    $scriptPath = Join-Path (Get-Item $PSScriptRoot).Parent.Parent.FullName "scripts\start-lmstudio-local.ps1"
}

if (Test-Path $scriptPath) {
    & $scriptPath @args
} else {
    Write-Error "Script start-lmstudio-local.ps1 não encontrado."
    exit 1
}
exit $LASTEXITCODE
