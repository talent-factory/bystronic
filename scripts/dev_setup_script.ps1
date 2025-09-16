# Development Environment Setup Script
# Installiert Python 3.x, git und uv fuer neue Mitarbeiter

Write-Host "=== Entwicklungsumgebung Setup ===" -ForegroundColor Green
Write-Host "Installiert: Python 3.x, git, uv" -ForegroundColor Yellow

# Ueberpruefe Administrator-Rechte
if (-NOT ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "FEHLER: Dieses Script muss als Administrator ausgefuehrt werden!" -ForegroundColor Red
    Write-Host "Rechtsklick auf PowerShell -> 'Als Administrator ausfuehren'" -ForegroundColor Yellow
    Read-Host "Druecken Sie Enter zum Beenden"
    exit 1
}

# Funktion fuer Fehlerbehandlung
function Test-CommandExists {
    param($Command)
    try {
        Get-Command $Command -ErrorAction Stop
        return $true
    }
    catch {
        return $false
    }
}

try {
    # 1. Chocolatey installieren (falls nicht vorhanden)
    Write-Host "`n[1/4] ??berpr??fe Chocolatey..." -ForegroundColor Cyan

    if (!(Test-CommandExists "choco")) {
        Write-Host "Chocolatey wird installiert..." -ForegroundColor Yellow
        Set-ExecutionPolicy Bypass -Scope Process -Force
        [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
        Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

        # PATH aktualisieren
        $env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")
    } else {
        Write-Host "Chocolatey ist bereits installiert." -ForegroundColor Green
    }

    # 2. Python installieren
    Write-Host "`n[2/4] Installiere Python..." -ForegroundColor Cyan
    choco install python -y
    if ($LASTEXITCODE -ne 0) { throw "Python Installation fehlgeschlagen" }

    # 3. Git installieren
    Write-Host "`n[3/4] Installiere Git..." -ForegroundColor Cyan
    choco install git -y
    if ($LASTEXITCODE -ne 0) { throw "Git Installation fehlgeschlagen" }

    # 4. UV installieren
    Write-Host "`n[4/4] Installiere uv..." -ForegroundColor Cyan

    # PATH f??r aktuelle Session aktualisieren
    $env:PATH = [System.Environment]::GetEnvironmentVariable("PATH","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("PATH","User")

    # uv ??ber pip installieren (nach Python Installation)
    python -m pip install --upgrade pip
    python -m pip install uv

    if ($LASTEXITCODE -ne 0) { throw "uv Installation fehlgeschlagen" }

    Write-Host "`n=== INSTALLATION ERFOLGREICH ===" -ForegroundColor Green
    Write-Host "Installierte Software:" -ForegroundColor White
    Write-Host "??? Python $(python --version 2>&1)" -ForegroundColor Green
    Write-Host "??? Git $(git --version)" -ForegroundColor Green
    Write-Host "??? uv $(uv --version)" -ForegroundColor Green

    Write-Host "`nHinweis: Starten Sie eine neue PowerShell/CMD-Sitzung, um alle Tools zu verwenden." -ForegroundColor Yellow
} catch {
    Write-Host "`nFEHLER: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host "Installation wurde abgebrochen." -ForegroundColor Red
}

Write-Host "`nDruecken Sie Enter zum Beenden..." -ForegroundColor Gray
$null = Read-Host
