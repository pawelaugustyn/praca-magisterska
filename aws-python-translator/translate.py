import boto3
import os

translate = boto3.client('translate')
s3 = boto3.client('s3')

SOURCE = os.environ['SOURCE']
TARGET = os.environ['TARGET']

def start(event, context):
    response = translate.translate_text(
        Text=event['sourceText'],
        SourceLanguageCode=SOURCE,
        TargetLanguageCode=TARGET
    )
    event['translatedText'] = response['TranslatedText']
    event['translatedLanguage'] = TARGET

    return event