from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Board(db.Model):
    __tablename__ = 'board'
    no = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    resdate = db.Column(db.DateTime, default=db.func.current_timestamp())
    hits = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'no': self.no,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'resdate': self.resdate.strftime('%Y-%m-%d %H:%M:%S'),
            'hits': self.hits
        }

class Member(db.Model):
    __tablename__ = 'member'
    id = db.Column(db.String(50), primary_key=True)
    pw = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    birth = db.Column(db.Date, nullable=False)
    email = db.Column(db.String(255), nullable=False)
    tel = db.Column(db.String(20))
    addr1 = db.Column(db.String(255))
    addr2 = db.Column(db.String(255))
    postcode = db.Column(db.String(10))
    regdate = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        return {
            'id': self.id,
            'pw': self.pw,
            'name': self.name,
            'birth': self.birth.strftime('%Y-%m-%d'),
            'email': self.email,
            'tel': self.tel,
            'addr1': self.addr1,
            'addr2': self.addr2,
            'postcode': self.postcode,
            'regdate': self.regdate.strftime('%Y-%m-%d %H:%M:%S')
        }

class Qna(db.Model):
    __tablename__ = 'qna'
    qno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lev = db.Column(db.Integer, default=0)
    parno = db.Column(db.Integer)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    author = db.Column(db.String(255))
    resdate = db.Column(db.DateTime, default=db.func.current_timestamp())
    hits = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'qno': self.qno,
            'lev': self.lev,
            'parno': self.parno,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'resdate': self.resdate.strftime('%Y-%m-%d %H:%M:%S'),
            'hits': self.hits
        }

class Dataroom(db.Model):
    __tablename__ = 'dataroom'
    dno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    author = db.Column(db.String(255))
    datafile = db.Column(db.String(255))
    resdate = db.Column(db.DateTime, default=db.func.current_timestamp())
    hits = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'dno': self.dno,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'datafile': self.datafile,
            'resdate': self.resdate.strftime('%Y-%m-%d %H:%M:%S'),
            'hits': self.hits
        }

class Product(db.Model):
    __tablename__ = 'product'
    pno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cate = db.Column(db.String(255))
    pname = db.Column(db.String(255))
    pcontent = db.Column(db.Text)
    img1 = db.Column(db.String(255))
    img2 = db.Column(db.String(255))
    img3 = db.Column(db.String(255))
    resdate = db.Column(db.DateTime, default=db.func.current_timestamp())
    hits = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'pno': self.pno,
            'cate': self.cate,
            'pname': self.pname,
            'pcontent': self.pcontent,
            'img1': self.img1,
            'img2': self.img2,
            'img3': self.img3,
            'resdate': self.resdate.strftime('%Y-%m-%d %H:%M:%S'),
            'hits': self.hits
        }