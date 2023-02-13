import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('userTable')

# Exceptions
class InvalidJson(Exception):
    pass


def lambda_handler(event, context):
    totalPoints=event["total"]['points']
    userid=event["data"]["userid"]
    try:
        if(totalPoints):
            table.update_item(
                Key={'usedid':userid},
                UpdateExpression="set points = :points",
                ExpressionAttributeValues={
                    ':points': totalPoints
                }
            )
    except Exception as e:
        print(e)
        raise(e)