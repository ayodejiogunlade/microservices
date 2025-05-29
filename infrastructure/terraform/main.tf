# Terraform Root Module for TechFlow Solutions

# Example: EKS Cluster
resource "aws_eks_cluster" "main" {
  name     = "techflow-eks"
  role_arn = var.eks_role_arn
  vpc_config {
    subnet_ids = var.subnet_ids
  }
}

# Example: RDS Instance
resource "aws_db_instance" "main" {
  allocated_storage    = 20
  engine              = "postgres"
  instance_class      = "db.t3.micro"
  name                = var.db_name
  username            = var.db_user
  password            = var.db_password
  parameter_group_name= "default.postgres15"
  skip_final_snapshot = true
  storage_encrypted   = true
  kms_key_id          = var.kms_key_id
  backup_retention_period = 7
}

# Example: Redis (Elasticache)
resource "aws_elasticache_cluster" "main" {
  cluster_id           = "techflow-redis"
  engine               = "redis"
  node_type            = "cache.t3.micro"
  num_cache_nodes      = 1
  parameter_group_name = "default.redis7"
}

# Example: AmazonMQ
resource "aws_mq_broker" "main" {
  broker_name = "techflow-mq"
  engine_type = "ActiveMQ"
  engine_version = "5.17.6"
  host_instance_type = "mq.t3.micro"
  publicly_accessible = false
  users {
    username = var.mq_user
    password = var.mq_password
  }
}

# Example: Secure secrets using AWS Secrets Manager
variable "db_password" {
  description = "Database password (stored in AWS Secrets Manager)"
  type        = string
  sensitive   = true
}

# Example: Enable encryption for EKS node group volumes
resource "aws_eks_node_group" "main" {
  # ...existing code...
  disk_encryption = true
  # ...existing code...
}

# Example: Use spot instances for cost optimization
resource "aws_eks_node_group" "spot" {
  # ...existing code...
  capacity_type = "SPOT"
  # ...existing code...
}

# Example: Add network policy for Kubernetes
resource "kubernetes_network_policy" "default-deny" {
  metadata {
    name      = "default-deny"
    namespace = "default"
  }
  spec {
    pod_selector = {}
    policy_types = ["Ingress", "Egress"]
  }
}

# Example: Add IAM policy for least privilege
resource "aws_iam_policy" "service_least_privilege" {
  name        = "service-least-privilege"
  description = "Least privilege policy for microservices"
  policy      = file("policies/service-least-privilege.json")
}

# Example: Enable automated backups for RDS
resource "aws_db_instance" "main" {
  # ...existing code...
  backup_retention_period = 7
  # ...existing code...
}

# Example: Add blue/green deployment strategy (documented for CI/CD)
# See cicd/github-actions/ci-cd-pipeline.yml for blue/green deployment steps
