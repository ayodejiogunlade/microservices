# CI/CD Pipeline for TechFlow Solutions Microservices

This folder contains configuration and documentation for the continuous integration and deployment (CI/CD) pipelines powering the microservices platform.

## Structure
- `github-actions/` — GitHub Actions workflows for build, test, deploy
- `scripts/` — Utility scripts for automation

## Key Pipelines
- **Build & Test:** Lint, test, and build all microservices on pull request and push
- **Docker Image Build:** Build and push Docker images to ECR or Docker Hub
- **Kubernetes Deploy:** Deploy updated services to EKS using rolling updates
- **Security & Compliance:** Run security scans and compliance checks

## Example Workflow (GitHub Actions)
```yaml
name: CI/CD Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
      - name: Build Docker image
        run: docker build -t ${{ github.repository }} .
      # ... more steps for push, deploy, etc.
```

## Monitoring & Rollback
- Integrated with AWS CloudWatch and Prometheus for monitoring
- Automated rollback on failed deployments

## Blue/Green Deployment Example
- Use separate blue and green namespaces in Kubernetes
- Deploy new version to green, run tests, then switch traffic
- Rollback by switching traffic back to blue

## Canary Deployment Example
- Use weighted routing in ALB or Istio
- Gradually increase traffic to new version
- Rollback if error rate increases

## Security Scanning
- Use Trivy or Snyk to scan Docker images for vulnerabilities
- Run scans in CI/CD pipeline

## See Also
- [`../docs/operations-runbook.md`](../docs/operations-runbook.md)
- [`../docs/security-compliance.md`](../docs/security-compliance.md)
