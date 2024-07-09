from flask import Blueprint, jsonify, request
from services.qna_service import QnaService

qna_bp = Blueprint('qna', __name__)

@qna_bp.route('/company/qna/list', methods=['GET'])
def get_qnas():
    qnas = QnaService.get_all_qnas()
    return jsonify([qna.to_dict() for qna in qnas])

@qna_bp.route('/company/qna/detail/<int:qna_id>', methods=['GET'])
def get_qna(qna_id):
    qna = QnaService.get_qna_by_id(qna_id)
    if qna:
        return jsonify(qna.to_dict())
    return jsonify({'message': 'Qna not found'}), 404

@qna_bp.route('/company/qna/insert', methods=['POST'])
def insert_qna():
    data = request.json
    qna = QnaService.create_qna(data)
    return jsonify(qna.to_dict())

@qna_bp.route('/company/qna/answer/<int:qna_id>', methods=['POST'])
def answer_qna(qna_id):
    data = request.json
    answer = QnaService.answer_qna(qna_id, data)
    if answer:
        return jsonify(answer.to_dict())
    return jsonify({'message': 'Qna not found'}), 404

@qna_bp.route('/company/qna/edit/<int:qna_id>', methods=['POST'])
def update_qna(qna_id):
    data = request.json
    qna = QnaService.update_qna(qna_id, data)
    if qna:
        return jsonify(qna.to_dict())
    return jsonify({'message': 'Qna not found'}), 404

@qna_bp.route('/company/qna/delete/<int:qna_id>', methods=['POST'])
def delete_qna(qna_id):
    success = QnaService.delete_qna(qna_id)
    if success:
        return jsonify({'message': 'Qna deleted successfully'})
    return jsonify({'message': 'Qna not found'}), 404
