class Player:
    id: str
    name: str
    courts: list

    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

    def join_court(self, court_num: int):
        if len(self.courts) < 3:
            self.courts.append(court_num)
            return 1
        return 0

    def leave_court(self, court_num: int):
        try:
            self.courts.remove(court_num)
            return 1
        except ValueError:
            return 0


