import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('bookTable')

class BookOutOfStock(ValueError):
    pass
class BookNotFound(Exception):
    pass

def isBookAvailable(book,quantity):
    return (int(book["quantity"])-quantity)>0

def lambda_handler(event, context):
    bookid=event["bookid"]
    quantity=event["quantity"]
    
    try:
        response= table.get_item(
            Key={"bookid":bookid}
        )
        book=response["Item"]
        
        if(isBookAvailable(book,quantity)):
            return book
        else:
            raise BookOutOfStock(f"The book {bookid} is out of stock")
        
    except BookOutOfStock as e:
        print(e)
        raise(e)
    except Exception as e:
        print(e)
        raise BookNotFound(f"the book {bookid} was not found")