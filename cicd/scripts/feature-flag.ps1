#!/usr/bin/env pwsh
# Script: feature-flag.ps1
# Description: Toggle feature flag for migration/cutover

param(
    [string]$FlagName,
    [string]$FlagValue
)

# Example: Store feature flag in AWS SSM Parameter Store
aws ssm put-parameter --name "/feature-flags/$FlagName" --value $FlagValue --type String --overwrite
