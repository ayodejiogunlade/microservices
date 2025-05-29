#!/usr/bin/env pwsh
# Script: dual-write.ps1
# Description: Simulate dual-write to monolith and microservice during migration

param(
    [string]$MonolithApiUrl,
    [string]$MicroserviceApiUrl,
    [string]$Payload
)

# Write to monolith
Invoke-RestMethod -Uri $MonolithApiUrl -Method POST -Body $Payload -ContentType 'application/json'
# Write to microservice
Invoke-RestMethod -Uri $MicroserviceApiUrl -Method POST -Body $Payload -ContentType 'application/json'
