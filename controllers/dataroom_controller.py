from flask import Blueprint, jsonify, request
from services.dataroom_service import DataroomService

dataroom_bp = Blueprint('dataroom', __name__)

@dataroom_bp.route('/company/dataroom/list', methods=['GET'])
def get_datarooms():
    datarooms = DataroomService.get_all_datarooms()
    return jsonify([dataroom.to_dict() for dataroom in datarooms])

@dataroom_bp.route('/company/dataroom/detail/<int:dataroom_id>', methods=['GET'])
def get_dataroom(dataroom_id):
    dataroom = DataroomService.get_dataroom_by_id(dataroom_id)
    if dataroom:
        return jsonify(dataroom.to_dict())
    return jsonify({'message': 'Dataroom not found'}), 404

@dataroom_bp.route('/company/dataroom/upload', methods=['POST'])
def insert_dataroom():
    data = request.json
    dataroom = DataroomService.create_dataroom(data)
    return jsonify(dataroom.to_dict())

@dataroom_bp.route('/company/dataroom/update/<int:dataroom_id>', methods=['POST'])
def update_dataroom(dataroom_id):
    data = request.json
    dataroom = DataroomService.update_dataroom(dataroom_id, data)
    if dataroom:
        return jsonify(dataroom.to_dict())
    return jsonify({'message': 'Dataroom not found'}), 404

@dataroom_bp.route('/company/dataroom/delete/<int:dataroom_id>', methods=['POST'])
def delete_dataroom(dataroom_id):
    success = DataroomService.delete_dataroom(dataroom_id)
    if success:
        return jsonify({'message': 'Dataroom deleted successfully'})
    return jsonify({'message': 'Dataroom not found'}), 404
