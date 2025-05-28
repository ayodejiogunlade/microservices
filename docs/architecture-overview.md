# Architecture Overview

## Service Decomposition
- Payment Processing Service
- User Management Service
- Wallet Service
- Notification Service
- Analytics Service
- Merchant Onboarding Service

## Infrastructure
- Amazon EKS (Kubernetes)
- Application Load Balancer (ALB)
- Amazon RDS (with read replicas)
- Amazon MQ
- Redis Cluster
- Service Mesh (App Mesh/Istio)

## Security & Compliance
- PCI DSS isolation for payment service
- Data residency controls
- Automated security scanning

## DevOps
- CI/CD per service
- Blue-green deployments
- Monitoring & alerting
