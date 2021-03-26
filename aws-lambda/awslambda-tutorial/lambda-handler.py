def lambda_handler(event, context):
    message = f"Hello {event['first_name']} {event['last_name']}!"
    return {
        'message': message
    }
print(lambda_handler({'first_name': 'Jiyun', 'last_name': 'Chung'}, 'hi'))
