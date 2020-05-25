from .s3 import File
from src.common.image import Img
import base64
import logging
import json
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

    img = Img(file.get(), event)
    try:
        img.change()
    except Exception as e:
        response = {
            "statusCode": 400,
            "body": json.dumps({"message": str(e)})
        }
        return response
        
    response = {
        "statusCode": 200,
        "body": base64.b64encode(img.getBytes().getvalue()),
        "headers": {
            'Content-Type': 'image/jpeg',
            'Cache-Control': 'public, max-age=31536000',
        },
        "isBase64Encoded": True
    }
    return _response(response, event)

def putImage(event):
    return _response(501, "")

def modifyImage(event):
    return _response(501, "")

def removeImage(event):
    return _response(501, "")
