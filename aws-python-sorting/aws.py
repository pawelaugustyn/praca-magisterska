from sorter import Sorter
import json

def start(event, context):
    sorter = Sorter()
    times = sorter.sort()

    return {
        "statusCode": 200,
        "body": json.dumps(times)
    }
    