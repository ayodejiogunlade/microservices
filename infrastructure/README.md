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
