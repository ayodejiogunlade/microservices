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
