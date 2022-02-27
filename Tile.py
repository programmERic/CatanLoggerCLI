class Tile:

    VALID_TILE_RESOURCE = ["w", "b", "s", "t", "o"]

    def __init__(self, tile, tile_num=None):
        self.value = tile 
        self.number = tile_num

        if tile == "desert":
            self.frequency = '7'
            self.resource = 'DES'
            return

        tile_len = len(tile)
        if tile_len == 2:
            frequency, resource = tile[0], tile[1]
        elif tile_len == 3:
            frequency, resource = tile[0:2], tile[2]
        else:
            raise Exception("Invalid tile format. {t}".format(t=tile))

        if not frequency.isdigit():
            raise Exception("Invalid tile format. Frequency of tile is not an integer. Frequency received: {f}".format(f=frequency))
        if resource not in Tile.VALID_TILE_RESOURCE:
            raise Exception("Invalid tile format. Resource of tile is not valid. Expected: {resources} but received Resource: {r} ".format(resources=Tile.VALID_TILE_RESOURCE.join(","), r=resource))
        
        self.frequency = frequency
        self.resource = resource

    def __str__(self):
        # tile = str(self.frequency + self.resource)
        # if len(tile) == 2: 
        #     tile = ' ' + tile
        # return '/---\\\n|' + tile + '|\n\\---/'
        return "({num})={val}".format(num=self.number, val=self.value)

    def __eq__(self, other):
        return self.value == other.value and self.number == other.number