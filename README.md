# PyTorch Inference Example

This project demonstrates how to deploy a PyTorch model using AWS services, including AWS Lambda and Amazon ECR. The solution includes containerization with Docker, unit tests with pytest, CI/CD pipeline using GitHub Actions, and Infrastructure as Code (IaC) with Terraform.

## Project Structure

```plaintext
pytorch-inference-example/
├── .github/
│   └── workflows/
│       └── aws-main.yaml          # GitHub Actions workflow for CI/CD
├── terraform/                     # Directory for Terraform configurations
├── Dockerfile                     # Dockerfile for building the container image
├── inference.py                   # Script for loading and inferring with the model
├── main.py                        # FastAPI application for serving the model
├── test_inference.py              # Unit tests for the inference script
├── requirements.txt               # Python dependencies
├── doubleit_model.pt              # Pretrained PyTorch model in TorchScript format
└── README.md                      # Project documentation
```

## Getting Started

### Prerequisites
* Python 3.10
* Docker
* AWS CLI
* Terraform
* Git


## GitHub Actions CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/aws-main.yaml`) automates the following steps:

1. **Build and test the application.**
2. **Build and push the Docker image to Amazon ECR.**
3. **Deploy the image to AWS Lambda.**

### Workflow Dispatch

You can manually trigger the workflow using the `workflow_dispatch` event.

## DISCLAIMER

I am aware that the project structure could have been better organized with a more hierarchical approach, separating components appropriately. However, due to time constraints, I was unable to refactor the structure as desired.

## Solution Overview

This solution uses AWS as the cloud service provider. The key components are:

- **AWS Lambda:** To serve the PyTorch model as a microservice.
- **Amazon ECR:** To store the Docker image of the application.

The provided Dockerfile and Terraform configuration ensure that the model can be deployed efficiently and managed through infrastructure as code.
