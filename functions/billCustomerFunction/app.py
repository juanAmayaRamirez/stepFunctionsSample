import json
import boto3

def lambda_handler(event, context):
    # billing can be done with some pse, paypal, nequi, API, here just return success
    return "sucessfully billed"