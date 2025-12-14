import uuid

class Member:
    health = 100

    def __init__(self, name, moves, types):
        self.name = name
        # moves should be a list of moves
        self.moves = moves
        # custom type
        self.type = type

        self.id = uuid.uuid1()