from models import db, Member

class MemberService:
    @staticmethod
    def get_all_members():
        return Member.query.all()

    @staticmethod
    def get_member_by_id(member_id):
        return Member.query.get(member_id)

    @staticmethod
    def create_member(data):
        new_member = Member(
            id=data['id'],
            pw=data['pw'],
            name=data['name'],
            birth=data['birth'],
            email=data['email'],
            tel=data['tel'],
            addr1=data['addr1'],
            addr2=data['addr2'],
            postcode=data['postcode']
        )
        db.session.add(new_member)
        db.session.commit()
        return new_member

    @staticmethod
    def update_member(member_id, data):
        member = Member.query.get(member_id)
        if member:
            member.pw = data['pw']
            member.name = data['name']
            member.birth = data['birth']
            member.email = data['email']
            member.tel = data['tel']
            member.addr1 = data['addr1']
            member.addr2 = data['addr2']
            member.postcode = data['postcode']
            db.session.commit()
            return member
        return None

    @staticmethod
    def delete_member(member_id):
        member = Member.query.get(member_id)
        if member:
            db.session.delete(member)
            db.session.commit()
            return True
        return False

    @staticmethod
    def login(data):
        member = Member.query.filter_by(id=data['id'], pw=data['pw']).first()
        return member is not None

    @staticmethod
    def logout(data):
        # Implement logout logic if needed
        pass
