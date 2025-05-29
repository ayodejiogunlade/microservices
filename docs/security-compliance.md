# Security & Compliance Mapping

- PCI DSS isolation for payment service
- Data encryption in transit (TLS) and at rest (RDS, Redis, AmazonMQ)
- Service mesh (AppMesh/Istio) for secure inter-service communication (mTLS)
- Automated vulnerability scanning in CI/CD (see `cicd/github-actions/ci-cd-pipeline.yml`)
- Use AWS Secrets Manager or SSM Parameter Store for secrets
- Data residency enforcement
