output "lambda_function_name" {
  description = "The name of the Lambda function"
  value       = aws_lambda_function.pytorch_inference_api.function_name
}

output "ecr_repository_url" {
  description = "The URL of the ECR repository"
  value       = aws_ecr_repository.pytorch_inference_api.repository_url
}