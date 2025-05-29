#!/usr/bin/env pwsh
# Script: migration-script.ps1
# Description: Example data migration script (monolith to microservice)

param(
    [string]$SourceDbConnection,
    [string]$TargetApiUrl
)

# Example: Export data from source DB (pseudo-code)
# $data = Invoke-Sqlcmd -ConnectionString $SourceDbConnection -Query "SELECT * FROM users"
# foreach ($row in $data) {
#     $payload = $row | ConvertTo-Json
#     Invoke-RestMethod -Uri $TargetApiUrl -Method POST -Body $payload -ContentType 'application/json'
# }
