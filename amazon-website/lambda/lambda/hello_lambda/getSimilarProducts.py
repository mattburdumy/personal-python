from __future__ import print_function

import boto3
import json, requests, base64, urllib, hashlib, hmac, datetime, pytz

print('Loading function')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
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
    return respond(None,event['test'])
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

def make_request():
    endpoint = 'webservices.amazon.com'
    uri = "/onca/xml"
    url = 'http://webservices.amazon.com/onca/xml'
    awsSecretKey = 'VSYix7/jZOMY9L26yboAI4I63dCx9HHUBhDW1qUa'
    timestamp = datetime.datetime.now(tz=pytz.UTC).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-4] + "Z"
    params = {
        'Service':'AWSECommerceService',
        'Operation': 'ItemSearch',
        'AWSAccessKeyId': 'AKIAJ7OJKPO3XIUZ6V4A',
        'AssociateTag': 'bestbo03-20',
        'Keywords': 'Harry+Potter',
        'SearchIndex':'Books',
        'ResponseGroup': "Images,ItemAttributes,Offers",
        "Sort" : "price",
        "Timestamp": timestamp
    }
    keys = sorted(params)
    slug = ""
    for key in keys:
        slug = slug + urllib.quote_plus(key) + '=' + urllib.quote_plus(params[key])
        if key != keys[-1]:
            slug = slug + '&'

    string_to_sign = "GET\n" + endpoint + "\n" + uri + "\n" + slug
    sha_hash = hmac.new(key=awsSecretKey, msg=string_to_sign,digestmod=hashlib.sha256)
    signature = base64.b64encode(sha_hash.digest())
    params['Signature'] = signature

    r = requests.get(url=url, params=params)
    print(r.text)
    pass
def main():
    # with open('test-event.json', 'r') as fp:
    #     data = json.load(fp)
    #     response = lambda_handler(event = data, context=None)
    #     print(response)
    make_request()

if __name__ == '__main__':
    main()
    print ("Script Complete")
