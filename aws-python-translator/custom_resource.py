import boto3
import cfn_resource
import re
handler = cfn_resource.Resource()

client = boto3.client('ses')

@handler.create
def create(event, context):
    address = event['ResourceProperties']['Email']
    if not identity_exists(address):
        client.verify_email_identity(
            EmailAddress=address
        )
    return {
        'Status': 'SUCCESS',
        'PhysicalResourceId': prepare_physical_id(address),
        'Data': {}
    }

@handler.update
def update(event, context):
    return {
        'Status': 'SUCCESS',
        'PhysicalResourceId': prepare_physical_id(event['PhysicalResourceId']),
        'Data': {}
    }

@handler.delete
def delete(event, context):
    address = event['ResourceProperties']['Email']
    if identity_exists(address):
        client.delete_identity(
            Identity=address
        )
    return {
        'Status': 'SUCCESS',
        'PhysicalResourceId': prepare_physical_id(event['PhysicalResourceId']),
        'Data': {}
    }

def prepare_physical_id(address):
    return re.sub(r'[^A-Za-z0-9 ]+', '', address)

def identity_exists(address):
    identities = get_identities()
    return address in identities
    
def get_identities():
    paginator = client.get_paginator("list_identities")
    pages = paginator.paginate(IdentityType='EmailAddress')
    identities = []
    for page in pages:
        identities.extend([identity for identity in page['Identities']])
    return identities
