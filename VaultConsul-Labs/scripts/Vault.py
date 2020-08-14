from hvac import Client
from os import getenv

client   = Client(
            url='http://localhost:8200',
            token='s.x3cBNKobC84wB82nvu09dIMI',
            verify=False
            )
MONGODB_USER = client.read("secret/devops-lab/app-devops")['data']['mongodb_user']
MONGODB_PASS = client.read("secret/devops-lab/app-devops")['data']['mongodb_pass']
REDIS_PASS   = client.read("secret/devops-lab/app-devops")['data']['redis_pass']

print("UserMongo: {} \nPassMongo: {}".format(MONGODB_USER, MONGODB_PASS))
print("PassRedis:",REDIS_PASS)