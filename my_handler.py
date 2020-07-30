import boto3
import time
import logging
import uuid
from boto3.dynamodb.conditions import Key
def my_handler(event, context):
    message = event
    expiryTimestamp = int(time.time() +200)
    client = boto3.resource('dynamodb')
    table = client.Table("csye6225")
    username = event['Records'][0]['Sns']['MessageAttributes']['username']['Value']
    token = event['Records'][0]['Sns']['MessageAttributes']['token']['Value']
    try:
        response = table.scan()
        for x,y in response.items():
            if x=='Items':
                for a in y:
                    for c,d in a.items():
                        if c=='username' and d==username:
                            return 0
    except Exception as e:
        print(e)
    else:
        id=uuid.uuid1()
        table.put_item(Item= {'id':str(id) ,'username':  username , 'token':token , 'TimeToExist': (expiryTimestamp) })
        SENDER = "support@prod.kmvanesa.me"
        RECIPIENT = username
        AWS_REGION = "us-east-1"
        SUBJECT = "Password Reset Link"
        BODY_TEXT = ("Your Link to Reset Password : https://prod.kmvanesa.me/password/{a}/{b} ".format(a=username,b=token))
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
    # print(event)
    return(message)