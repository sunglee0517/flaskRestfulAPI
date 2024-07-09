from models import db, Dataroom

class DataroomService:
    @staticmethod
    def get_all_datarooms():
        return Dataroom.query.all()

    @staticmethod
    def get_dataroom_by_id(dataroom_id):
        return Dataroom.query.get(dataroom_id)

    @staticmethod
    def create_dataroom(data):
        new_dataroom = Dataroom(
            title=data['title'],
            content=data['content'],
            author=data['author'],
            datafile=data['datafile']
        )
        db.session.add(new_dataroom)
        db.session.commit()
        return new_dataroom

    @staticmethod
    def update_dataroom(dataroom_id, data):
        dataroom = Dataroom.query.get(dataroom_id)
        if dataroom:
            dataroom.title = data['title']
            dataroom.content = data['content']
            dataroom.datafile = data['datafile']
            db.session.commit()
            return dataroom
        return None

    @staticmethod
    def delete_dataroom(dataroom_id):
        dataroom = Dataroom.query.get(dataroom_id)
        if dataroom:
            db.session.delete(dataroom)
            db.session.commit()
            return True
        return False
