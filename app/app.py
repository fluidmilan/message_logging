def lambda_handler(event, context):
    from message_logging import log_messages
    import json
    log_messages('Hello world')
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": 'return' # invoke layer function
        }),
    }

