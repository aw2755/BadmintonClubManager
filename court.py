class Court:
    court_num: int
    players: list

    def __init__(self, court_num: int):
        self.court_num = court_num
        self.players = []

    def add_player(self, player: str) -> int:
        if len(self.players) <= 4:
            self.players.append(player)
            return 1
        return 0

    def remove_player(self, player: str) -> int:
        if player in self.players:
            self.players.remove(player)
            return 1
        return 0

    def has(self, player_id: int) -> bool:
        if player_id in self.players:
            return True
        return False
