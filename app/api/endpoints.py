from flask import request, jsonify, Response
from sqlalchemy.orm.exc import NoResultFound

from app import db
from app.api import api
from app.models import Tasks
from app.schema import TaskSchema
from marshmallow import ValidationError


@api.route('/tasks')
def result():
    
    records = [row.to_dict() for row in Tasks.get_all_tasks()] # paginate
        
    return jsonify({"result":  records})


@api.route('/task', methods=['POST'])
def postTask():

    data = request.json

    try:
        TaskSchema().load(data)
    except ValidationError as err:
        return jsonify(err.messages), 422
   
    task = Tasks(data['name'], data['status']).save()

    return jsonify({"result": task.to_dict()}), 201


@api.route('/task/<id>', methods=['PUT'])
def putTask(id):

    data = request.json

    try:
        TaskSchema().load(data)
    except ValidationError as err:
        return jsonify(err.messages), 422
    
    try:
        task = Tasks(**data).update(id)
    except NoResultFound:
        return jsonify({"err_msg": "task id not found"}), 404

    return jsonify({"result": task.to_dict()}), 200


@api.route('/task/<id>', methods=['DELETE'])
def deleteTask(id):

    try:
        Tasks.delete(id)
    except NoResultFound:
        return jsonify({"err_msg": "task id not found"}), 404

    return Response(status=200)


@api.teardown_request
def teardown_request(exception):
    if exception:
        db.session.rollback()
    db.session.remove()