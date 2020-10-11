import boto3
import botocore
import json
from collections import namedtuple
from src.aws.handler import (
    listImages,
    getImage,
    putImage,
    removeImage
)

handlers = {
    '/images': {
        "GET": listImages
    },
    '/images/{image}': {
        "GET": getImage,
        "PUT": putImage,
        "DELETE": removeImage
    }
}

def start(event, context):
    try:
        handler = handlers[event['resource']][event['httpMethod']]
    except KeyError as err:
        print(err)
        return wrongRequest()
    
    return handler(event)

def wrongRequest():
    return {
        "statusCode": 400,
        "body": json.dumps({
            "error": "Wrong method or resource"
        })
    }

def get_log_event(e):
    to_log = {x: e.get(x) for x in ('resource', 'path', 'httpMethod', 'pathParameters', 'body')}
    to_log['requestId'] = e['requestContext']['requestId']
    return to_log
