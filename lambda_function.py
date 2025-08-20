import json

def lambda_handler(event, context):
    # TODO implement
    a="aman"
    b="shreya"
    return {
        'name':a,
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!....... (Modified v0.2')
    }