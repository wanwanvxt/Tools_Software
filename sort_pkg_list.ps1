function Sort-CsvFile {
  param (
    [string]$FilePath
  )

  if (!(Test-Path $FilePath)) {
    Write-Host "File does not exist!"
    return
  }

  $lines = Get-Content -Path $FilePath -Encoding UTF8
  if ($lines.Count -eq 0) {
    Write-Host "File is empty!"
    return
  }

  $header = $lines[0]
  $rows = $lines[1..($lines.Count - 1)]

  $sortedRows = $rows |
    Sort-Object {
      ($_.Split(',')[0].Trim().ToLower())
    }

  $output = @()
  $output += $header
  $output += $sortedRows

  Set-Content -Path $FilePath -Value $output -Encoding UTF8

  Write-Host "CSV sorted"
}

Sort-CsvFile -FilePath "./pkg.csv"