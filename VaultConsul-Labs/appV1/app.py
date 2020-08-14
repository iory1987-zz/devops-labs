# -*- coding: latin-1 -*-
#####################################
# Author: David Ferreira Gonçalves
# Email: iory1987@gmail.com
# GitHub: iory987
# Date: 10/08/2020
#####################################
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

import logging
from flask import Flask, request, jsonify
from flask_restplus import Api, Resource

from tools import HealthVault, HealthConsul, HealthMongoDB, HealthRabbitMQ

from pymongo import MongoClient
from pika import PlainCredentials, ConnectionParameters, BlockingConnection

flask_app = Flask(__name__)
if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    flask_app.logger.handlers = gunicorn_logger.handlers
    flask_app.logger.setLevel(gunicorn_logger.level)

app = Api(app = flask_app)

name_space = app.namespace('api', description='Main API')
@name_space.route('/')
class MainClass(Resource):
    def get(self):
        try:
            uri = "mongodb://{0}:{1}@{2}/?authSource={3}&authMechanism={4}".format(
                'Uther',
                'ArthasLichKing',
                'localhost',
                'admin',
                'SCRAM-SHA-1')
            client = MongoClient(uri)
            db = client['devops-lab']
            collection=db['lab']
            cursor = collection.find({})
            ms = []
            for document in cursor:
                ms.append(document['name'])
            flask_app.logger.info('get all data from mongo')
            print(ms)
            return jsonify({"data": ms})
        except Exception as e:
            flask_app.logger.error(e)
            return {"message":"error to get data from mongo"}

    def post(self):
        message = request.json['data']
        try:
            credentials = PlainCredentials('illidan', 'SylvanaWindRunner')
            parameters  = ConnectionParameters('localhost', 5672, '/', credentials)
            connection = BlockingConnection(parameters)
            channel = connection.channel()
            channel.queue_declare(queue='devops-labs')
            channel.basic_publish(exchange='', routing_key='devops-labs', body=message)
            connection.close()
            flask_app.logger.info('message put on rabbit')
            return {"message": 'message put on rabbit'}, 201
        except Exception as e:
            flask_app.logger.error(e)
            return {"message":"error to put message on rabbit"}

@name_space.route("/health", methods=['GET'])
class HealthClass(Resource):
    def get(self):
        mongodb = HealthMongoDB()
        rabbitmq = HealthRabbitMQ()
        vault = HealthVault()
        consul = HealthConsul()
        return {"status":"Healthy",
                "results": [
                {"Vaut":vault},
                {"Consul":consul},
                {"MongoDB":mongodb},
                {"RabbitMQ":rabbitmq}
                ]
            }