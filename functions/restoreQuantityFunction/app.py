import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('bookTable')

# Exceptions
class InvalidJson(Exception):
    pass


def lambda_handler(event, context):
    orderQuantity=event["data"]['quantity']
    bookid=event["data"]["bookid"]
    try:
        table.update_item(
            Key={'usedid':bookid},
            UpdateExpression="set quantity = :quantity",
            ExpressionAttributeValues={
                ':quantity': orderQuantity
            }
        )
        return "Quantity restored"
    except Exception as e:
        print(e)
        raise(e)