def my_handler(event, context):
    message = 'Hello AWS{} {}!'.format(event['first_name'], 
                                    event['last_name'])  
    return { 
        'message' : message
    }  