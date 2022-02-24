class Robber:
    ROBBER = None

    def __init__(self):
        if not Robber.ROBBER:
            Robber.ROBBER = self
        self.tile = "desert"

    def rob(self, tile):
        self.tile = tile