import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('bookTable')

# stepfunctions = boto3.client('stepfunctions')

def updateBookQuantity(bookid,orderQuantity):
    table.update_item(
        Key={'bookid':bookid},
        UpdateExpression="SET quantity = quantity - :orderQuantity",
        ExpressionAttributeValues={
            ':orderQuantity': orderQuantity
        }
    )
def lambda_handler(event, context):
    print(event)
    try:
        record= event['Records'][0]
        body= json.loads(record['body'])
        # courier= "sampleemail@email.com"

        updateBookQuantity(body['data']['bookid'],body['data']['quantity'])

        # stepfunctions.send_task_success(
        #     taskToken=body['Token'],
        #     output=json.dumps({courier})
        # )

    except Exception as e:
        print(e)
        # stepfunctions.send_task_failure(
        #     taskToken=body['Token'],
        #     error='NoCourierAvailable',
        #     cause='No Couriers are available'
        # )