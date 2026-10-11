<#
.SYNOPSIS
Fetch the aiworkspace harness with a shallow clone and run its installer, so a target repo
never needs a manual checkout of the harness.

.EXAMPLE
Downloaded to a file and run directly:
    .\bootstrap.ps1 -RepoUrl <repo-url> -Target <target-repo>

.EXAMPLE
As a one-liner, piped straight from a raw URL (PowerShell needs the wrapper below to pass
parameters through a piped script block):
    iex "& { $(irm <raw-url-of-this-script>) } -RepoUrl <repo-url>"

RepoUrl can be omitted if $env:AIWORKSPACE_REPO_URL is set. Target defaults to the current
directory. Any arguments after -Target are forwarded to install.py (e.g. --dry-run, --force).
The clone is removed when the script exits, whether or not the install succeeds.
#>
[CmdletBinding()]
param(
    [string]$RepoUrl = $env:AIWORKSPACE_REPO_URL,
    [string]$Target = ".",
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$InstallArgs
)

$ErrorActionPreference = "Stop"

if (-not $RepoUrl) {
    Write-Error "RepoUrl is required (pass -RepoUrl or set `$env:AIWORKSPACE_REPO_URL)"
    exit 2
}

function Resolve-Python {
    # Windows commonly shadows the real interpreter with a non-functional App Execution
    # Alias stub of the same name earlier on PATH, so check every match (-All), not just
    # the first, and confirm a candidate actually runs before trusting it.
    foreach ($name in "python3", "python") {
        foreach ($cmd in (Get-Command $name -All -ErrorAction SilentlyContinue)) {
            try {
                & $cmd.Source --version 2>&1 | Out-Null
                if ($LASTEXITCODE -eq 0) { return $cmd.Source }
            } catch {}
        }
    }
    return $null
}

$pythonExe = Resolve-Python
if (-not $pythonExe) { Write-Error "python (3.8+) is required"; exit 1 }
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { Write-Error "git is required"; exit 1 }

$tmp = Join-Path ([System.IO.Path]::GetTempPath()) ([System.IO.Path]::GetRandomFileName())
New-Item -ItemType Directory -Path $tmp | Out-Null
try {
    $harnessDir = Join-Path $tmp "harness"
    git clone --depth 1 --quiet $RepoUrl $harnessDir
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
    $installScript = [System.IO.Path]::Combine($harnessDir, "tools", "install.py")
    & $pythonExe $installScript $Target @InstallArgs
    exit $LASTEXITCODE
}
finally {
    Remove-Item -Recurse -Force $tmp -ErrorAction SilentlyContinue
}
