# AWS Connect and Web Application Deployment

This project contains CloudFormation templates for deploying Amazon Q, Amazon Connect instance and a web application infrastructure.


## Architecture

![Architecture](/Images/architecture.png)

The architecture for this solution is described as follows

1.	Users in Okta are configured to be federated to AWS IAM Identity Center.
2.	When user clicks on chat in web application, the Amazon Q Business application will authenticate users against Okta as identity source through Amazon IAM Identity Center, create a session and stores it Amazon Q application.
3.	Amazon Q business application will fetch knowledge from the Amazon S3 Data source to answer questions or generate summaries. 
4.	Amazon Q custom plugin uses Open API schema to discover and understand the capabilities of the Amazon API Gateway API.
5.	OAuth information is stored in AWS Secrets Manager and provide the Secret information to the plugin.
6.	Plugin assumes IAM role to access the secrets in AWS Secret Manager.
7.	When user wants to send a case, the custom plugin invokes API hosted on the Amazon API Gateway. 
8.	Amazon API Gateway uses the same Okta user’s session and authorizes the access.
9.	Amazon API Gateway will then invoke AWS Lambda to create a case in Amazon Connect.
10.	AWS Lambda hosted in Amazon Virtual Private Cloud (VPC) internally calls  Amazon Connect  API via  Amazon Connect VPC Interface Endpoint powered by AWS PrivateLink. 
11.	The contact center agents can also use Amazon Q in Connect to further assist the user. 


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

1.  AWS CLI configured with appropriate permissions
2.  Access to create resources in Amazon Connect, EC2, ECR, CodeBuild, and Lambda
3.  Source code for the web application available at the specified `SourceZipUrl`
4.	Have a valid AWS account. 
5.	Have Okta developer account, setup an application and API. If you do not have an Okta please see below instructions.
6.	Have an Amazon Q Business Pro subscription to create Amazon Q apps. 
7.	Have the service-linked IAM role AWSServiceRoleForQBusiness. If you don’t have one, create it with the qbusiness.amazonaws.com service name.
8.	Have an AWS Identity and Access Management (IAM) role in the account that has sufficient permissions to create the necessary resources. If you have administrator access to the account, no action is required.
9.	Enable AWS Cloudtrail logging for operational and risk auditing.
10.	Enable Budget policy notification to protect customer from unwanted billing.


## Cleanup

To avoid incurring future charges, delete the resources that you created and clean up your account.
You can clean up the AWS environment using the following steps:
1.	Empty the contents of the S3 buckets you created as part of the CloudFormation stack.
2.	Delete the CloudFormation stack you created as part of this post.
3.	Disable the application from AWS IAM Identity Center.


## Notes

- The web application is built using Angular and containerized using Docker.
- The CodeBuild project automatically builds and pushes the Docker image to ECR.
- VPC Flow Logs are enabled and encrypted using KMS for enhanced security.

For more detailed information about each component, refer to the individual CloudFormation template files.


