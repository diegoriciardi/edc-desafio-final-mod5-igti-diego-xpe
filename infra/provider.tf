# Centralizar o arquivo de controle de estado fo Terraform
terraform {
  backend "s3" {
    bucket = "terraform-state-igti-diego-xpe-desafio-final-mod5"
    key = "state/igti/edc/desafio-final/mod5/terraform.tfstate"
    region = "us-east-1"
  }
}