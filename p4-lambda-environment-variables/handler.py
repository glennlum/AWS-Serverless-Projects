import os
import json


def printEnv(event, context):
    '''Returns all environment variables'''
    env_variables = ['ENV_VARIABLE_1', 'ENV_VARIABLE_2', 'ENV_VARIABLE_3']
    return [os.environ[i] for i in env_variables]
