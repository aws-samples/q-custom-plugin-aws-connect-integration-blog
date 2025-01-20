'''
=================================== Apache License ===========================
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

================================================================================

'''


# AWS Lambda function 
import boto3
import json
import os
import logging
from functools import lru_cache

MAX_CASE_NAME_LENGTH=100;

amazon_connect = boto3.client('connect')

# Initialize clients at module level with caching
@lru_cache(maxsize=None)
def get_connect_cases_client():
    amazon_connect_cases_client = boto3.client('connectcases', endpoint_url=f'https://{ENV_VARS["CASES_VPC_ENDPOINT"]}')
    return amazon_connect_cases_client
    
@lru_cache(maxsize=None)
def get_sts_client():
    return boto3.client('sts')

@lru_cache(maxsize=1)
def get_account_id() -> str:
    """Cache and return AWS account ID."""
    return get_sts_client().get_caller_identity()["Account"]

ENV_VARS = {
    'INSTANCE_ID': os.environ.get('INSTANCE_ID'),
    'DOMAIN_ID': os.environ.get('DOMAIN_ID'),
    'TEMPLATE_ID': os.environ.get('TEMPLATE_ID'),
    'AWS_REGION': os.environ.get('AWS_REGION'),
    'DOMAIN_NAME': os.environ.get('DOMAIN_NAME'),
    'CUSTOMER_ID': os.environ.get('CUSTOMER_ID'),
    'AGENT_ID': os.environ.get('AGENT_ID'),
    'CASES_VPC_ENDPOINT': os.environ.get('CASES_ENDPOINT_DNSNAMES')
}

#validate environment variables
def validate_env_vars() -> None:
    """Validate all required environment variables are present."""
    missing_vars = [key for key, value in ENV_VARS.items() if value is None]
    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

#Validate case name
def validate_case_name( case_name) -> None:
        """Validates case name for security and constraints."""
        if not case_name:
            raise ValueError("Case name is missing")
        
        if len(case_name) > MAX_CASE_NAME_LENGTH:
            raise ValueError("Case name exceeds maximum length")
    
        #  XSS script validation
        if '<script>' in case_name:
            raise ValueError("Case name contains XSS attack")



# lambda code to make amazon connect api call
def lambda_handler(event, context):
    
    # create logger object
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    

    # Validate environment variables
    validate_env_vars()

    logger.info("in the lambda function")
   
    try:
       
        #log an event object
        logger.info(f'event: {event}')
        
        # Get case name from request
        case_name = event.get('name')
        logger.info(f'Case name: {case_name}')
        validate_case_name(case_name)
    
        # Get account ID (cached)     
        account_Id= get_account_id()
        logger.info(f'account_id: {account_Id}')


                        
        response4 = get_connect_cases_client().create_case(
            domainId=ENV_VARS["DOMAIN_ID"],
            fields=[
                 {
                    'id': 'customer_id',
                    'value': {
                        'stringValue': f'arn:aws:profile:{ENV_VARS["AWS_REGION"]}:{account_Id}:domains/{ENV_VARS["DOMAIN_NAME"]}/profiles/{ENV_VARS["CUSTOMER_ID"]}'
                        
                    }
                    
                 } ,
                 {
                    'id': 'title',
                    'value': {
                        'stringValue': case_name
                        
                    }
                 },
                 {
                    'id': 'assigned_user',
                    'value': {
                         'stringValue': f'arn:aws:connect:{ENV_VARS["AWS_REGION"]}:{account_Id}:instance/{ENV_VARS["INSTANCE_ID"]}/agent/{ENV_VARS["AGENT_ID"]}'
                        
                    }   
                 
                    
                 }
                 
            ],
            templateId=ENV_VARS["TEMPLATE_ID"]
        ) 
        
        logger.info(f'response: {response4}')
        return {
            'statusCode': 200,
            'body': json.dumps('Case created successfully!')
        }
       
       
    except Exception as e:
        logger.info(f'error while creating case: {e}')
        return {
            'statusCode': 500,
            'body': json.dumps('failed to create case. Please contact your admin' )
        }
    