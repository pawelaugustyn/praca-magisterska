import boto3
import json
import os

sf = boto3.client('stepfunctions')

def start(event, context):
    entry = event['Records'][0]
    bucket = entry['s3']['bucket']['name']
    key = entry['s3']['object']['key']

    response = sf.start_execution(
        stateMachineArn=os.environ['SF_ARN'],
        input=json.dumps({
            "bucket": bucket,
            "key": key
        })
    )
    print(response['executionArn'])
