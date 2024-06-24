provider "aws" {
  region = var.aws_region
}

resource "aws_ecr_repository" "pytorch_inference_api" {
  name = "pytorch-inference-api"
}

resource "aws_lambda_function" "pytorch_inference_api" {
  function_name = "pytorch-inference-api"
  image_uri     = "${aws_ecr_repository.pytorch_inference_api.repository_url}:latest"

  package_type = "Image"
  role         = aws_iam_role.lambda_exec_role.arn

  lifecycle {
    ignore_changes = [image_uri]
  }
}

resource "aws_iam_role" "lambda_exec_role" {
  name = "lambda_exec_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      },
    ]
  })

  inline_policy {
    name   = "ecr_pull_policy"
    policy = jsonencode({
      Version = "2012-10-17"
      Statement = [
        {
          Action = [
            "ecr:GetDownloadUrlForLayer",
            "ecr:BatchGetImage",
            "ecr:BatchCheckLayerAvailability"
          ]
          Effect   = "Allow"
          Resource = "*"
        }
      ]
    })
  }
}