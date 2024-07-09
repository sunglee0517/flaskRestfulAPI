from models import db, Board

class BoardService:
    @staticmethod
    def get_all_boards():
        return Board.query.all()

    @staticmethod
    def get_board_by_id(board_id):
        return Board.query.get(board_id)

    @staticmethod
    def create_board(data):
        new_board = Board(
            title=data['title'],
            content=data['content'],
            author=data['author']
        )
        db.session.add(new_board)
        db.session.commit()
        return new_board

    @staticmethod
    def update_board(board_id, data):
        board = Board.query.get(board_id)
        if board:
            board.title = data['title']
            board.content = data['content']
            db.session.commit()
            return board
        return None

    @staticmethod
    def delete_board(board_id):
        board = Board.query.get(board_id)
        if board:
            db.session.delete(board)
            db.session.commit()
            return True
        return False
