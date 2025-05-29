# Infrastructure as Code for TechFlow Solutions Microservices

This folder contains Terraform and Kubernetes manifests for provisioning and managing AWS infrastructure and EKS workloads.

## Structure
- `terraform/` — Terraform modules for AWS resources (EKS, RDS, Redis, AmazonMQ, VPC, IAM, etc.)
- `k8s/` — Kubernetes manifests for microservices, ingress, config, and service mesh

## Getting Started

### Prerequisites
- [Terraform](https://www.terraform.io/downloads.html)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- AWS CLI configured with appropriate credentials

### Usage
```powershell
cd infrastructure/terraform
terraform init
terraform apply

cd ../k8s
kubectl apply -f .
```

## Security & Compliance
See [`../docs/security-compliance.md`](../docs/security-compliance.md) for details on IAM, VPC, and secrets management.

## Cost Analysis
See [`../docs/cost-analysis.md`](../docs/cost-analysis.md) for infrastructure cost breakdown and optimization strategies.

## Blue/Green Deployments
- Use two environments (blue and green) for zero-downtime deployments
- Route traffic using ALB or Kubernetes Ingress
- Switch traffic after health checks pass
- Rollback by switching back to previous environment

## Canary Deployments
- Gradually shift traffic to new version using weighted routing
- Monitor error rates and rollback if needed

## Disaster Recovery
- Automated RDS backups and multi-AZ
- EKS node group auto-recovery
- Documented restore procedures

## Secrets Management
- Store secrets in AWS Secrets Manager or SSM Parameter Store
- Reference secrets in Terraform and Kubernetes manifests
