from PIL import UnidentifiedImageError
from .s3 import File
from src.common.image import Img
import base64
import logging
import json
logger = logging.getLogger()
logger.setLevel(logging.INFO)

QUERY_STRING_PARAMETERS = "queryStringParameters"

def _response(response, event):
    event['response'] = response
    print(event)
    return response

def _return_message(code, message):
    return {
        "statusCode": code,
        "body": json.dumps({"message": message})
    }

def listImages(event):
    objs = File.list()
    return _return_message(200, objs)

def getImage(event):
    file = File(event['pathParameters']['image'])
    if not file.exists():
        return _return_message(404, "not found")

    img = Img(file.get(), event, QUERY_STRING_PARAMETERS)
    try:
        img.change()
    except Exception as e:
        return _return_message(400, str(e))
        
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
    file = File(event['pathParameters']['image'])
    if file.exists():
        return _return_message(409, "Key already exists")
    body = event['body']
    try:
        img = Img(base64.b64decode(body), event, QUERY_STRING_PARAMETERS)
    except UnidentifiedImageError:
        return _return_message(400, "wrong image type")
    file.put(img.getBytes(), img.format)
    
    return _return_message(201, "created")

def modifyImage(event):
    return _response(501, "")

def removeImage(event):
    file = File(event['pathParameters']['image'])
    if not file.exists():
        return _return_message(404, "not found")
    file.delete()
    return _return_message("200", "deleted")
