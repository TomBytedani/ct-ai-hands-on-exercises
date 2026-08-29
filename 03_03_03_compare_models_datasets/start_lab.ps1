[CmdletBinding()]
param(
    [switch]$NoBrowser
)

$ErrorActionPreference = 'Stop'

$labRoot = $PSScriptRoot
$environmentRoot = Join-Path $env:LOCALAPPDATA 'CTAIStudy'
$environmentPath = Join-Path $environmentRoot 'lab-3-3-3'
$environmentPython = Join-Path $environmentPath 'Scripts\python.exe'
$requirementsPath = Join-Path $labRoot 'requirements.txt'
$notebookPath = Join-Path $labRoot 'guided_lab.ipynb'

if (-not (Test-Path -LiteralPath $environmentPython)) {
    Write-Host "Creating the isolated lab environment at $environmentPath"
    New-Item -ItemType Directory -Force -Path $environmentRoot | Out-Null
    python -m venv $environmentPath
    if ($LASTEXITCODE -ne 0) {
        throw 'Python could not create the virtual environment.'
    }
}

Write-Host 'Checking the lab dependencies...'
& $environmentPython -m pip install --disable-pip-version-check --requirement $requirementsPath
if ($LASTEXITCODE -ne 0) {
    throw 'The lab dependencies could not be installed.'
}

$jupyterArguments = @(
    '-m', 'jupyter', 'lab', $notebookPath,
    "--ServerApp.root_dir=$labRoot"
)

if ($NoBrowser) {
    $jupyterArguments += '--no-browser'
}

Write-Host 'Starting JupyterLab. Stop it with Ctrl+C in this window.'
& $environmentPython @jupyterArguments
