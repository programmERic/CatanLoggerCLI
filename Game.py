import Player
import Robber
import Tile

DEBUG = True

class Game:

    VALID_DICE_NUM = [2, 3, 4, 5, 6, 8, 9, 10, 11, 12]
    VALID_RESOURCE_NAME = ["w", "b", "s", "t", "o",\
                                "wood", "brick", "sheep", "wheat", "ore"]
    VALID_TOTAL_RESOURCE_HEX = {"w":4, "b":3, "s":4, "t":4, "o":3}
    VALID_NUM_DIE_FREQ = {2:1, 3:2, 4:2, 5:2, 6:2, 8:2, 9:2, 10:2, 11:2, 12:1}

    VALID_NUM_RESOURCES = 18
    

    def __init__(self):

        self.board = None
        self.board_vals = []
        self.num_players = 4
        self.players = []
        self.robber = Robber()

    def create_board(self, tiles):

        if DEBUG:
            print("create_board, tiles: {}".format(tiles))

        board = {freq:[] for freq in range(2, 13)}

        num_tiles = 0
        
        for tile in tiles.replace(" ", "").split(","):

            if tile == "desert":
                continue

            tile_len = len(tile)
            if tile_len == 2:
                frequency, resource = int(tile[0]), tile[1]
            elif tile_len == 3:
                frequency, resource = int(tile[0:2]), tile[2]
            else:
                raise Exception("Invalid tile format. {t}".format(t=tile))

            if frequency not in Game.VALID_DICE_NUM:
                raise Exception("Invalid hex dice number {freq}".format(freq=frequency))
            elif resource not in Game.VALID_RESOURCE_NAME:
                raise Exception("Invalid resource name {res}".format(res=resource))

            board[frequency] += resource
            num_tiles += 1

            self.board_vals.append(tile)
            
        if num_tiles!= Game.VALID_NUM_RESOURCES:
            raise Exception("Invalid number of resources on the board. Expected {}, but counted {}.".format(Game.VALID_NUM_RESOURCES, num_tiles))

        if DEBUG:
            print("create_board, board: {}".format(board))

        self.board = board
        return

    def handle_tiles_str(self, tile_str):
        if tile_str is None:
            return None
        tiles = []
        for freq_res_str in tile_str.split(","):
            new_tile = Tile(freq_res_str)
            tiles.append(new_tile)
        return tiles

    def add_players(self):
        for order in range(1, self.num_players+1):
            new_player = Player(order=order)
            self.players.append(new_player)
            print(new_player)

    def roll(self, dice):
        for player in self.players:
            player.cards_roll_resource(dice, self.robber)

    def resolve_player(self, player):
        for check_player in self.players:
            if player == str(check_player.order)\
               or player == "p" + str(check_player.order)\
               or player == check_player.name:
                return check_player

        raise Exception("Invalid player identifier: `{}`".format(player))

    def player_builds_or_buys_dev(self, player, purpose, tiles):
        curr_player = self.resolve_player(player)
        curr_player.use_cards(purpose=purpose, tiles=self.handle_tiles_str(tiles))

    def player_robs(self, player1, player2, tile):
        curr_player = self.resolve_player(player1)
        robbed_player = self.resolve_player(player2)
        curr_player.cards_rob_resource(robbed_player)

    def player_trades(self, player1, resources1, player2, resources2):
        curr_player1 = self.resolve_player(player1)
        curr_player2 = self.resolve_player(player2)

        curr_player1.cards_update_resource(resources1, award=False)
        curr_player1.cards_update_resource(resources2, award=True)

        curr_player2.cards_update_resource(resources2, award=False)
        curr_player2.cards_update_resource(resources1, award=True)

    def game_players(self):
        for player in self.players:
            print("P{order}-{name}".format(order=player.order, name=player.name))

    def game_player_name(self, player, name):
        self.resolve_player(player).name = name

    def game_cards(self):
        for player in self.players:
            print(player)

    def game_fix(self):
        pass

    def game_board(self):
        pass

        #for i in range([3, 4, 5, 4, 3]):
        #    padding = 