class Robber:
    ROBBER = None

    def __init__(self, tile):
        if not Robber.ROBBER:
            Robber.ROBBER = self
        self.tile = tile

    def rob(self, tile):
        self.tile = tile