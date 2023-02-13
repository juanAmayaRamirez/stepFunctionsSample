import json

def lambda_handler(event, context):
    total=event['book']['price']*event['data']['quantity']
    return {"total":total}