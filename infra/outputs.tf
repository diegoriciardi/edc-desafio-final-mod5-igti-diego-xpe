output "cluster_id" {
  description = "EKS cluster ID"
  value = module.eks.cluster_id
}

output "cluster_name" {
  description = "EKS cluster ID"
  value = local.cluster_name
}

output "cluster_endpoint" {
  description = "EKS cluster ID"
  value = module.eks.cluster_endpoint
}

output "region" {
  description = "AWS regionn"
  value = var.region
}