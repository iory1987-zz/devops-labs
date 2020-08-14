import consul

client = consul.Consul(host='localhost')
index = None
index, data = client.kv.get('devops-lab', index=index, recurse=True)
for k in data:
    print(k['Value'].decode("utf-8"))