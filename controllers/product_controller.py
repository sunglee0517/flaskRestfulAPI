from flask import Blueprint, jsonify, request
from services.product_service import ProductService

product_bp = Blueprint('product', __name__)

@product_bp.route('/company/products/list', methods=['GET'])
def get_products():
    products = ProductService.get_all_products()
    return jsonify([product.to_dict() for product in products])

@product_bp.route('/company/products/detail/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = ProductService.get_product_by_id(product_id)
    if product:
        return jsonify(product.to_dict())
    return jsonify({'message': 'Product not found'}), 404

@product_bp.route('/company/products/insert', methods=['POST'])
def insert_product():
    data = request.json
    product = ProductService.create_product(data)
    return jsonify(product.to_dict())

@product_bp.route('/company/products/update/<int:product_id>', methods=['POST'])
def update_product(product_id):
    data = request.json
    product = ProductService.update_product(product_id, data)
    if product:
        return jsonify(product.to_dict())
    return jsonify({'message': 'Product not found'}), 404

@product_bp.route('/company/products/delete/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    success = ProductService.delete_product(product_id)
    if success:
        return jsonify({'message': 'Product deleted successfully'})
    return jsonify({'message': 'Product not found'}), 404
