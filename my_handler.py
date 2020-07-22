def my_handler(event, context):
    message = 'Hello World,{} {}!'.format(event['first_name'], 
                                    event['last_name'])  
    return { 
        'message' : message
    }  