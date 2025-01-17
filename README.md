# AWS Connect and Web Application Deployment

This project contains CloudFormation templates for deploying an AWS Connect instance and a web application infrastructure.

## Repository Structure

```
.
├── childstack1.yml
├── childstack2.yml
├── parentstack.yml
└── README.md
```

## Main Components

1. `parentstack.yml`: Parent stack that manages two child stacks.
2. `childstack1.yml`: Creates an AWS Connect instance and related resources.
3. `childstack2.yml`: Sets up the web application infrastructure.

## Deployment Instructions

To deploy this project, use the AWS CloudFormation console or AWS CLI to create a stack using the `parentstack.yml` template. This will automatically create the child stacks for the AWS Connect instance and web application.

## Configuration Parameters

The `parentstack.yml` template accepts the following parameters:

- Environment
- Audience
- Issuer
- IdcInstanceArn
- PluginDisplayName
- ClientId
- ClientSecret
- AuthorizationUrl
- TokenUrl
- SourceZipUrl
- ContainerPort
- RepositoryName

Ensure you have the correct values for these parameters before deployment.

## Resources Created

### AWS Connect Instance (childstack1.yml)

- VPC with private subnets
- Amazon Connect instance
- Customer Profiles domain
- Hours of operation
- Custom security profile
- VPC Flow Logs

### Web Application (childstack2.yml)

- ECR repository
- CodeBuild project
- IAM roles and policies
- VPC with flow logs
- Lambda function for triggering CodeBuild
- KMS keys for encryption

## Prerequisites

Before deploying this project, ensure you have:

1. AWS CLI configured with appropriate permissions
2. Access to create resources in Amazon Connect, EC2, ECR, CodeBuild, and Lambda
3. Source code for the web application available at the specified `SourceZipUrl`

## Notes

- The web application is built using Angular and containerized using Docker.
- The CodeBuild project automatically builds and pushes the Docker image to ECR.
- VPC Flow Logs are enabled and encrypted using KMS for enhanced security.

For more detailed information about each component, refer to the individual CloudFormation template files.