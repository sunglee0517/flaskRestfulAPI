from flask import Blueprint, jsonify, request
from services.member_service import MemberService

member_bp = Blueprint('member', __name__)

@member_bp.route('/company/members/getMemberList', methods=['GET'])
def get_members():
    members = MemberService.get_all_members()
    return jsonify([member.to_dict() for member in members])

@member_bp.route('/company/members/getMember/<member_id>', methods=['GET'])
def get_member(member_id):
    member = MemberService.get_member_by_id(member_id)
    if member:
        return jsonify(member.to_dict())
    return jsonify({'message': 'Member not found'}), 404

@member_bp.route('/company/members/mypage/<member_id>', methods=['GET'])
def mypage(member_id):
    member = MemberService.get_member_by_id(member_id)
    if member:
        return jsonify(member.to_dict())
    return jsonify({'message': 'Member not found'}), 404

@member_bp.route('/company/members/join', methods=['POST'])
def join():
    data = request.json
    member = MemberService.create_member(data)
    return jsonify(member.to_dict())

@member_bp.route('/company/members/myInfoEdit/<member_id>', methods=['POST'])
def update_member(member_id):
    data = request.json
    member = MemberService.update_member(member_id, data)
    if member:
        return jsonify(member.to_dict())
    return jsonify({'message': 'Member not found'}), 404

@member_bp.route('/company/members/login', methods=['POST'])
def login():
    data = request.json
    if MemberService.login(data):
        return jsonify({'message': 'Login successful'})
    return jsonify({'message': 'Invalid credentials'}), 401

@member_bp.route('/company/members/logout', methods=['POST'])
def logout():
    data = request.json
    MemberService.logout(data)
    return jsonify({'message': 'Logout successful'})
