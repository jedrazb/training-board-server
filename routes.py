from flask import request, abort

from server import app, client
from queries import gql_create_model, gql_create_datapoint, gql_connect_datapoint_with_model


@app.route('/create_model', methods=['POST'])
def create_model():
    if not request.json:
        abort(400)

    model_name = request.json['name']

    response = client.execute(gql_create_model, {'name': model_name})

    return response['createModel']['id']


@app.route('/create_datapoint', methods=['POST'])
def create_datapoint():
    if not request.json:
        abort(400)

    payload = {
        'epoch': request.json['epoch'],
        'loss': request.json['loss'],
        'acc': request.json['acc']
    }

    response = client.execute(gql_create_datapoint, payload)

    return response['createDataPoint']['id']


@app.route('/relate_datapoint_to_model', methods=['POST'])
def relate_datapoint_to_model():
    if not request.json:
        abort(400)

    payload = {
        'modelModelId': request.json['model_id'],
        'dataPointsDataPointId': request.json['datapoint_id'],
    }

    client.execute(gql_connect_datapoint_with_model, payload)

    return 'success'
