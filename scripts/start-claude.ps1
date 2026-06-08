# Wrapper for Claude Launcher
# Procura o script no diretório raiz do projeto (um nível acima de scripts/)
$rootPath = (Get-Item $PSScriptRoot).Parent.FullName
$scriptPath = Join-Path $rootPath "scripts\start-claude-local.ps1"

# Se não encontrar no local relativo, tenta encontrar no diretório 'scripts' da raiz do workspace original
if (-not (Test-Path $scriptPath)) {
    $scriptPath = Join-Path (Get-Item $PSScriptRoot).Parent.Parent.FullName "scripts\start-claude-local.ps1"
}

if (Test-Path $scriptPath) {
    & $scriptPath @args
} else {
    Write-Error "Script start-claude-local.ps1 não encontrado."
    exit 1
}
exit $LASTEXITCODE
