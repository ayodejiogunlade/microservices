#!/usr/bin/env pwsh
# Script: deploy-all.ps1
# Deploy all microservices to EKS

kubectl apply -f ../infrastructure/k8s/payment-processing-service.yaml
# Add similar lines for other microservices
