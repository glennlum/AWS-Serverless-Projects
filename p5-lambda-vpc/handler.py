import json


def hello(event, context):
    body = {
        "message": "Invoked lambda within a VPC",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
