import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('userTable')

# Exceptions

class InvalidJson(Exception):
    pass


def deductpoints(userid):
    table.update_item(
        Key={'userid':userid},
        UpdateExpression="set points = :zero",
        ExpressionAttributeValues={
            ':zero': 0
        }
    )

def lambda_handler(event, context):
    try:
        userid=event["data"]["userid"]
        orderTotal=event["total"]["total"]
    except Exception as e:
        print(e)
        raise InvalidJson("Invalid Json format")
    try:
        response= table.get_item(
            Key={"userid":userid}
        )
        user=response["Item"]
        points=user["points"]
        if(orderTotal>points):
            deductpoints(userid)
            orderTotal=orderTotal-points
            return {"total":orderTotal,"points":points}
        else:
            raise Exception(f"Order total is less than redem points")
        
    except Exception as e:
        print(e)
        raise(e)