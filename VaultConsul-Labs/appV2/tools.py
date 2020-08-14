from os import getenv
from hvac import Client
from consul import Consul
from requests import get
from pymongo import MongoClient

def HealthVault():
    client = Client(url='http://{}:8200'.format(getenv('VAULT_SERVER')),verify=False)
    status = client.sys.read_health_status(method='GET')
    if status['initialized'] == True and status['sealed'] == False:
        return "Healthy"
    else:
        return "Unhealthy"

def HealthConsul():
    client = Consul(host=getenv('CONSUL_SERVER'))
    health = client.health.service('consul')[1][0]['Checks'][0]['Status']
    if health == 'passing':
        return "Healthy"
    else:
        return "Unhealthy"

def HealthMongoDB(HOST):
    try:
        client = MongoClient(HOST, 27017)
        status = client.db_name.command('ping')
        if status['ok'] == 1.0:
            return "Healthy"
    except:
        return "Unhealthy"

def HealthRabbitMQ(HOST, USER, PASS):
    status = get('http://{}:15672/api/aliveness-test/%2F'.format(HOST), auth=(USER, PASS))
    print()
    if status.json()['status'] == 'ok':
        return "Healthy"
    else:
        return "Unhealthy"

def GetCredentials():
    VAULT_SERVER  = getenv('VAULT_SERVER')
    VAULT_TOKEN   = getenv('VAULT_TOKEN')
    CONSUL_SERVER = getenv('CONSUL_SERVER')
    client = Client(
            url="http://{}:8200".format(VAULT_SERVER),
            token=VAULT_TOKEN,
            verify=False
            )
    MONGODB_USER = client.read("secret/devops-lab/app-devops")['data']['mongodb_user']
    MONGODB_PASS = client.read("secret/devops-lab/app-devops")['data']['mongodb_pass']
    RABBIT_USER  = client.read("secret/devops-lab/app-devops")['data']['rabbitmq_user']
    RABBIT_PASS  = client.read("secret/devops-lab/app-devops")['data']['rabbitmq_pass']
    client = Consul(host=CONSUL_SERVER)
    index, data = client.kv.get('devops-lab', index=None, recurse=True, separator='lab')
    CONFIG = [
        {"mongo": {"user": MONGODB_USER,"pass": MONGODB_PASS,"host": data[0]['Value'].decode("utf-8")}},
        {"rabbit":{"user": RABBIT_USER, "pass": RABBIT_PASS, "host": data[1]['Value'].decode("utf-8")}}
    ]
    return CONFIG