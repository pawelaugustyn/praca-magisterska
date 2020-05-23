from .s3 import File
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def _response(response, event):
    event['response'] = response
    print(event)
    return response

def getImage(event):
    file = File(event['pathParameters']['image'])
    if not file.exists():
        response = {
            "statusCode": 404,
            "body": ""
        }
        return _response(response, event)
        
    response = {
        "statusCode": 301,
        "body": "",
        "headers": {
            "location": file.url
        }
    }
    return _response(response, event)

def putImage(event):
    return _response(501, "")

def modifyImage(event):
    return _response(501, "")

def removeImage(event):
    return _response(501, "")
