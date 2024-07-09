from models import db, Product

class ProductService:
    @staticmethod
    def get_all_products():
        return Product.query.all()

    @staticmethod
    def get_product_by_id(product_id):
        return Product.query.get(product_id)

    @staticmethod
    def create_product(data):
        new_product = Product(
            cate=data['cate'],
            pname=data['pname'],
            pcontent=data['pcontent'],
            img1=data['img1'],
            img2=data['img2'],
            img3=data['img3']
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product

    @staticmethod
    def update_product(product_id, data):
        product = Product.query.get(product_id)
        if product:
            product.cate = data['cate']
            product.pname = data['pname']
            product.pcontent = data['pcontent']
            product.img1 = data['img1']
            product.img2 = data['img2']
            product.img3 = data['img3']
            db.session.commit()
            return product
        return None

    @staticmethod
    def delete_product(product_id):
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return True
        return False
