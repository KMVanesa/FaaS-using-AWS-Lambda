import boto3
def my_handler(event, context):
    dynamodb = boto3.client('dynamodb')
    table = client.Table("csye6225")
    print(table.table_status)
    message = 'Hello World,{}!'.format(event['Records'][0]['Sns']['Message'])  
    return { 
        'message' : message
    }  