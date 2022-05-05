import boto3

# Create a low-level service client by name using the default session.
client = boto3.client('lambda')


def listFunctions(event, context):
    '''returns a list of lambda functions in AWS'''
    response = client.list_functions()
    return response
