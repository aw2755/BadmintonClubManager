class Court:
    court_num: int
    players: list

    def __init__(self, court_num: int):
        self.court_num = court_num
        self.players = []

    def add_player(self, player_id: int) -> int:
        if player_id not in self.players:
            self.players.append(player_id)
            return 1
        return 0

    def remove_player(self, player_id: int) -> int:
        if player_id in self.players:
            self.players.remove(player_id)
            return 1
        return 0

    def has(self, player_id: int) -> bool:
        if player_id in self.players:
            return True
        return False
