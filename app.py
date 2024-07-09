from flask import Flask
from config import Config
from models import db
from controllers.board_controller import board_bp
from controllers.dataroom_controller import dataroom_bp
from controllers.qna_controller import qna_bp
from controllers.product_controller import product_bp
from controllers.member_controller import member_bp
from index import index_bp  # 홈 페이지 라우트 추가

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(board_bp)
app.register_blueprint(dataroom_bp)
app.register_blueprint(qna_bp)
app.register_blueprint(product_bp)
app.register_blueprint(member_bp)
app.register_blueprint(index_bp)  # 홈 페이지 블루프린트 등록

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
