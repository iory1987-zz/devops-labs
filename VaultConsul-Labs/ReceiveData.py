from pika import PlainCredentials, ConnectionParameters, BlockingConnection
from pymongo import MongoClient

credentials = PlainCredentials('illidan', 'SylvanaWindRunner')
parameters  = ConnectionParameters('localhost', 5672, '/', credentials)
connection  = BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='devops-labs')


for method_frame, properties, body in channel.consume('devops-labs'):
    uri = "mongodb://{0}:{1}@{2}/?authSource={3}&authMechanism={4}".format(
                'Uther',
                'ArthasLichKing',
                'localhost',
                'admin',
                'SCRAM-SHA-1')
    client = MongoClient(uri)
    db = client['devops-lab']
    collection = db['lab']
    data = {"name": body.decode("utf-8")}
    result = collection.insert(data)
    print(data)
    print(result)
    channel.basic_ack(method_frame.delivery_tag)

requeued_messages = channel.cancel()
channel.close()
connection.close()