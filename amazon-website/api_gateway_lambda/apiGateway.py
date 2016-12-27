from __future__ import print_function

import boto3
import json

print('Loading function')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else res,
        'headers': {
            'Content-Type': 'text/html',
        },
    }


def lambda_handler(event, context):
    '''Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.

    To scan a DynamoDB table, make a GET request with the TableName as a
    query string parameter. To put, update, or delete an item, make a POST,
    PUT, or DELETE request respectively, passing in the payload to the
    DynamoDB API as a JSON body.
    '''
    #print("Received event: " + json.dumps(event, indent=2))
    # return respond(err=None,res=get_index_file())
    return respond(err=None,res=get_index_file())
    # operations = {
    #     'DELETE': lambda dynamo, x: dynamo.delete_item(**x),
    #     'GET': lambda dynamo, x: dynamo.scan(**x),
    #     'POST': lambda dynamo, x: dynamo.put_item(**x),
    #     'PUT': lambda dynamo, x: dynamo.update_item(**x),
    # }
    #
    # operation = event['httpMethod']
    # if operation in operations:
    #     payload = event['queryStringParameters'] if operation == 'GET' else json.loads(event['body'])
    #     dynamo = boto3.resource('dynamodb').Table(payload['TableName'])
    #     return respond(None, operations[operation](dynamo, payload))
    # else:
    #     return respond(ValueError('Unsupported method "{}"'.format(operation)))

def get_index_file():
    session = boto3.Session()
    client = session.client('s3')
    obj =client.get_object(Bucket='recowebsite', Key='dummyData.txt')
    return (obj['Body'].read())


def main():
    # with open('test-event.json', 'r') as fp:
    #     data = json.load(fp)
    #     response = lambda_handler(event=data, context=None)
    #     print(response)
    print(get_index_file())

if __name__ == '__main__':
    main()
    print ("Script Complete")
