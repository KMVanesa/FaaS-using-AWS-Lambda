import boto3
import time
def my_handler(event, context):
    expiryTimestamp = int(time.time() +15*60)
    client = boto3.resource('dynamodb')
    table = client.Table("csye6225")
    print(table.table_status)
    message = 'Hello World,{}!'.format(event['Records'][0]['Sns']['Message']) 
    table.put_item(Item= {'id': '1','message':  message , 'TimeToExist': (expiryTimestamp) })
    SENDER = "support@prod.kmvanesa.me"
    RECIPIENT = "vkrutarth@gmail.com"
    AWS_REGION = "us-east-1"
    SUBJECT = "Password Reset Link"
    BODY_TEXT = (" Link : www.google.com ")
    CHARSET = "UTF-8"
    emailclient = boto3.client('ses',region_name=AWS_REGION)
    response = emailclient.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': CHARSET,
                    'Data': BODY_TEXT,
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
    )
    return { 
        'message' : message
    }