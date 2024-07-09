from flask import Blueprint, jsonify, request
from services.board_service import BoardService

board_bp = Blueprint('board', __name__)

@board_bp.route('/company/boards/list', methods=['GET'])
def get_boards():
    boards = BoardService.get_all_boards()
    return jsonify([board.to_dict() for board in boards])

@board_bp.route('/company/boards/detail/<int:board_id>', methods=['GET'])
def get_board(board_id):
    board = BoardService.get_board_by_id(board_id)
    if board:
        return jsonify(board.to_dict())
    return jsonify({'message': 'Board not found'}), 404

@board_bp.route('/company/boards/insert', methods=['POST'])
def insert_board():
    data = request.json
    board = BoardService.create_board(data)
    return jsonify(board.to_dict())

@board_bp.route('/company/boards/update/<int:board_id>', methods=['POST'])
def update_board(board_id):
    data = request.json
    board = BoardService.update_board(board_id, data)
    if board:
        return jsonify(board.to_dict())
    return jsonify({'message': 'Board not found'}), 404

@board_bp.route('/company/boards/delete/<int:board_id>', methods=['POST'])
def delete_board(board_id):
    success = BoardService.delete_board(board_id)
    if success:
        return jsonify({'message': 'Board deleted successfully'})
    return jsonify({'message': 'Board not found'}), 404