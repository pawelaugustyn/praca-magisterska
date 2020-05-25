import boto3
import os
from io import BytesIO

s3 = boto3.client('s3')

class File:
    BUCKET = os.environ["BUCKET"]
    REGION = os.environ["REGION"]

    def __init__(self, name):
        self.__name = name

    def exists(self):
        response = s3.list_objects_v2(
            Bucket=File.BUCKET,
            Prefix=self.__name,
        )
        for obj in response.get('Contents', []):
            if obj['Key'] == self.__name:
                return True

        return False

    @property
    def url(self):
        return f"https://{File.BUCKET}.s3.{File.REGION}.amazonaws.com/{self.__name}"

    def get(self):
        response = s3.get_object(
            Bucket=File.BUCKET,
            Key=self.__name,
        )
        return response["Body"].read()
