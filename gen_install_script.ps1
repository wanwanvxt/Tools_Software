function Generate-InstallScript {
  param (
      [string]$CsvFile,
      [string]$OutputScript = "install.ps1"
  )

  if (!(Test-Path $CsvFile)) {
      Write-Host "CSV file not found."
      return
  }

  $lines = Get-Content -Path $CsvFile -Encoding UTF8
  if ($lines.Count -lt 2) {
      Write-Host "Invalid CSV format or empty file."
      return
  }

  $commands = @()
  $header = $lines[0]
  $dataRows = $lines[1..($lines.Count - 1)]

  foreach ($line in $dataRows) {
      if ([string]::IsNullOrWhiteSpace($line)) { continue }

      $cols = $line -split ','

      $pkg = $cols[0].Trim()
      $params = if ($cols.Count -gt 1) { $cols[1].Trim() } else { "" }
      $installArgs = if ($cols.Count -gt 2) { $cols[2].Trim() } else { "" }
      $addnParams = if ($cols.Count -gt 3) { $cols[3].Trim() } else { "" }

      $cmd = "choco install $pkg"
      if ($params) { $cmd += " --params `"`'$params`'`"" }
      if ($installArgs) { $cmd += " --install-arguments `"`'$installArgs`'`"" }
      $cmd += " -y $addnParams"

      $commands += $cmd
  }

  $outputLines = @(
      "Set-ExecutionPolicy Bypass -Scope Process -Force",
      "`$ErrorActionPreference = 'Stop'",
      ""
  ) + $commands

  Set-Content -Path $OutputScript -Value $outputLines -Encoding UTF8

  Write-Host "Generated install script."
}

Generate-InstallScript -CsvFile "./pkg.csv"