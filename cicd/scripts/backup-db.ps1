#!/usr/bin/env pwsh
# Script: backup-db.ps1
# Description: Backup RDS database to S3

param(
    [string]$DbInstanceIdentifier,
    [string]$S3Bucket
)

aws rds create-db-snapshot --db-instance-identifier $DbInstanceIdentifier --db-snapshot-identifier "backup-$(Get-Date -Format yyyyMMddHHmmss)"
# Optionally, export snapshot to S3 (requires additional setup)
# aws rds export-db-snapshot-to-s3 --db-snapshot-identifier ... --s3-bucket-name $S3Bucket
