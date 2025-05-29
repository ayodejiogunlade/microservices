#!/usr/bin/env pwsh
# Script: restore-db.ps1
# Description: Restore RDS database from snapshot

param(
    [string]$DbInstanceIdentifier,
    [string]$DbSnapshotIdentifier
)

aws rds restore-db-instance-from-db-snapshot --db-instance-identifier $DbInstanceIdentifier --db-snapshot-identifier $DbSnapshotIdentifier
