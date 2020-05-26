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
            Prefix=self.__name
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
            Key=self.__name
        )
        return response["Body"].read()

    def put(self, body, format):
        s3.put_object(
            Bucket=File.BUCKET,
            Key=self.__name,
            Body=body,
        )

    def delete(self):
        s3.delete_object(
            Bucket=File.BUCKET,
            Key=self.__name
        )

    @staticmethod
    def list():
        paginator = s3.get_paginator("list_objects_v2")
        pages = paginator.paginate(Bucket=File.BUCKET)
        objects = []
        for page in pages:
            objects.extend([{"Key": obj["Key"], "Size": obj["Size"]} for obj in page["Contents"]])
        return objects
