import boto3
import os

ses = boto3.client('ses')
ADDRESS = os.environ['ADDRESS']

def start(event, context):
    resp = ses.send_email(
        Source=ADDRESS,
        Destination={
            "ToAddresses": [ADDRESS]
        },
        Message={
            "Subject": {
                "Data": f"Translation: {event['key']} from {event['sourceLanguage']} to {event['translatedLanguage']}"
            },
            "Body": {
                "Text": {
                    "Data": f"Original:\n{event['sourceText']}\n\nTranslated:\n{event['translatedText']}"
                }
            }
        }
    )

    event['messageId'] = resp['MessageId']
    return event
