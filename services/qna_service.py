from models import db, Qna

class QnaService:
    @staticmethod
    def get_all_qnas():
        return Qna.query.all()

    @staticmethod
    def get_qna_by_id(qna_id):
        return Qna.query.get(qna_id)

    @staticmethod
    def create_qna(data):
        new_qna = Qna(
            title=data['title'],
            content=data['content'],
            author=data['author']
        )
        db.session.add(new_qna)
        db.session.commit()
        return new_qna

    @staticmethod
    def answer_qna(qna_id, data):
        qna = Qna.query.get(qna_id)
        if qna:
            answer = Qna(
                lev=qna.lev + 1,
                parno=qna.qno,
                title=data['title'],
                content=data['content'],
                author=data['author']
            )
            db.session.add(answer)
            db.session.commit()
            return answer
        return None

    @staticmethod
    def update_qna(qna_id, data):
        qna = Qna.query.get(qna_id)
        if qna:
            qna.title = data['title']
            qna.content = data['content']
            db.session.commit()
            return qna
        return None

    @staticmethod
    def delete_qna(qna_id):
        qna = Qna.query.get(qna_id)
        if qna:
            db.session.delete(qna)
            db.session.commit()
            return True
        return False
