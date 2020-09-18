from handler import lambda_handler

result = lambda_handler(
    {
        'model_name': 'samplemodel',
        'operation': 'list',
        'payload': '',
    }
    , {})
print(result)
