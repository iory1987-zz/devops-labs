from hvac import Client
from consul import Consul
from requests import get
from pymongo import MongoClient

def HealthVault():
    client = Client(url='http://localhost:8200',verify=False)
    status = client.sys.read_health_status(method='GET')
    if status['initialized'] == True and status['sealed'] == False:
        return "Healthy"
    else:
        return "Unhealthy"

def HealthConsul():
    client = Consul(host='localhost')
    health = client.health.service('consul')[1][0]['Checks'][0]['Status']
    if health == 'passing':
        return "Healthy"
    else:
        return "Unhealthy"

def HealthMongoDB():
    try:
        client = MongoClient('localhost', 27017)
        status = client.db_name.command('ping')
        if status['ok'] == 1.0:
            return "Healthy"
    except:
        return "Unhealthy"

def HealthRabbitMQ():
    status = get('http://localhost:15672/api/aliveness-test/%2F', auth=('illidan', 'SylvanaWindRunner'))
    print()
    if status.json()['status'] == 'ok':
        return "Healthy"
    else:
        return "Unhealthy"
