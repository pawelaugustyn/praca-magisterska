import boto3

s3 = boto3.client('s3')
comprehend = boto3.client('comprehend')
VALID_LANGS = ("pl", "en")

def start(event, context):
    bucket = event['bucket']
    key = event['key']
    text = read_file(bucket, key)
    lang = get_source_language(bucket, key, text)

    event['sourceLanguage'] = lang
    event['sourceText'] = text
    return event

def get_source_language(bucket, key, text):
    name = ".".join(key.split(".")[:-1])
    if contains_lang_in_name(name):
        return name[-2:]
    response = comprehend.detect_dominant_language(Text=text)
    if len(response['Languages']) == 0:
        return None
    most_important = sorted(response['Languages'], key=lambda k: k['Score'], reverse=True)
    return most_important[0]['LanguageCode']

def read_file(bucket, key):
    response = s3.get_object(
        Bucket=bucket,
        Key=key
    )
    return response["Body"].read().decode('utf-8')

def contains_lang_in_name(name):
    if name[-3:] in [f"_{lang}" for lang in VALID_LANGS]:
        return True
    return False
