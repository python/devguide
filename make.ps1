# Command file for Sphinx documentation

param (
    [string]$target = "help"
)

Set-StrictMode -Version 3.0
$ErrorActionPreference = "Stop"

$BUILDDIR = "_build"
$SPHINXOPTS = "--fail-on-warning --keep-going"
$_ALL_SPHINX_OPTS = $SPHINXOPTS

$_PYTHON = $Env:PYTHON ?? "py -3"
$_SPHINX_BUILD = $Env:SPHINXBUILD ?? ".\venv\Scripts\sphinx-build"
$_SPHINX_LINT = $Env:SPHINXLINT ?? ".\venv\Scripts\sphinx-lint"
$_VENV_DIR = "venv"

function New-VirtualEnviromnent
{
    Write-Host "Creating venv in $_VENV_DIR"
    if (Get-Command "uv" -ErrorAction SilentlyContinue) {
        & uv venv $_VENV_DIR
        $Env:VIRTUAL_ENV = $_VENV_DIR
        & uv pip install -r requirements.txt
        Remove-Item Env:VIRTUAL_ENV
    } else {
        & $_PYTHON -m venv venv
        Write-Host "Installing requirements"
        & venv\Scripts\python -m pip install -r requirements.txt
        $Script:_PYTHON = "venv\Scripts\python"
    }
}

function Invoke-SphinxBuild
{
    param (
        [string]$BuilderName,
        [string]$BuildDir,
        [string]$Options
    )
    if (-Not (Test-Path -Path $_VENV_DIR)) { New-VirtualEnviromnent }
    & $_SPHINX_BUILD -M $BuilderName "." $BuildDir $Options.Split(" ")
}

function Invoke-Check {
    if (-Not (Test-Path -Path $_VENV_DIR)) { New-VirtualEnviromnent }
    & $_SPHINX_LINT -i tools -i venv --enable default-role
}

if ($target -Eq "help") {
    Write-Host "Please use `make <target>` where <target> is one of"
    Write-Host "  venv       to create a venv with necessary tools"
    Write-Host "  html       to make standalone HTML files"
    Write-Host "  linkcheck  to check all external links for integrity"
    Write-Host "  htmlview   to open the index page built by the html target in your browser"
    Write-Host "  clean      to remove the venv and build files"
    Write-Host "  check      to check for stylistic and formal issues using sphinx-lint"
    Write-Host "  versions   to update release cycle after changing release-cycle.json"
    Exit
}

if ($target -Eq "clean") {
    $ToClean = @(
        $BUILDDIR,
        $_VENV_DIR,
        "include/branches.csv", "include/end-of-life.csv", "include/release-cycle.svg"
    )
    foreach ($item in $ToClean) {
        if (Test-Path -Path $item) {
            Remove-Item -Path $item -Force -Recurse
        }
    }
    Exit $LASTEXITCODE
}

if ($target -Eq "check") {
    Invoke-Check
    Exit $LASTEXITCODE
}

if ($target -Eq "versions") {
    & $_PYTHON _tools/generate_release_cycle.py
    if ($LASTEXITCODE -Ne 0) { exit 1 }
    Write-Host "Release cycle data generated."
    Exit $LASTEXITCODE
}

if ($target -Eq "htmlview") {
    Invoke-SphinxBuild "html" "$BUILDDIR" "$_ALL_SPHINX_OPTS"
    if (Test-Path -Path "$BUILDDIR\html\index.html") {
        Write-Host "Opening $BUILDDIR\html\index.html in the default web browser..."
        Start-Process "$BUILDDIR\html\index.html"
    }
    Exit $LASTEXITCODE
}

Invoke-SphinxBuild "$target" "$BUILDDIR" "$_ALL_SPHINX_OPTS"
Exit $LASTEXITCODE
