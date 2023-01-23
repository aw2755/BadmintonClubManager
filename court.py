class Court:
    court_num: int
    players: set
    queue: list

    def __init__(self, id: int):
        self.id = id

    def add_player(self, player: str) -> int:
        if len(self.players) > 4:
            self.players.add(player)
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
