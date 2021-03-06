from Player import * 
from Robber import * 
from Tile import * 

DEBUG = True

class Game:

    VALID_DICE_NUM = [2, 3, 4, 5, 6, 8, 9, 10, 11, 12]
    VALID_RESOURCE_NAME = ["w", "b", "s", "t", "o"]#,\
                                #"wood", "brick", "sheep", "wheat", "ore"]
    VALID_TOTAL_RESOURCE_HEX = {"w":4, "b":3, "s":4, "t":4, "o":3}
    VALID_NUM_DIE_FREQ = {2:1, 3:2, 4:2, 5:2, 6:2, 8:2, 9:2, 10:2, 11:2, 12:1}

    VALID_NUM_RESOURCES = 19
    

    def __init__(self):

        self.board = {str(freq):[] for freq in range(2, 13)}
        self.board_tiles = []
        self.num_players = 4
        self.players = []
        self.robber = Robber("desert")
        #self.bank = Bank() #TODO: add bank
        '''
        if the board contains duplicates like 4w & 4w,
        then the user will need to specify the tile number 
        when calling rob, knight and other specific 
        tile-dependent commands
        '''
        self.require_tile_num = False 
        

    def create_board(self, tiles):

        if DEBUG:
            print("create_board, tiles: {}".format(tiles))

        duplicate_check = set()
        possible_duplicate_tiles = {}

        num_tiles = 0
        tile_values = tiles.replace(" ", "").split(",")

        for tile_num, tile_str in enumerate(tile_values, start=1):
            tile = Tile(tile_str, tile_num)
            duplicate_check.add(tile_str)
            self.board_tiles.append(tile)
            self.board[tile.frequency].append(tile.resource)
            num_tiles += 1

            if tile_str not in possible_duplicate_tiles:
                possible_duplicate_tiles[tile_str] = 0
            possible_duplicate_tiles[tile_str] += 1    
            
        if num_tiles != Game.VALID_NUM_RESOURCES:
            raise Exception("Invalid number of resources on the board. Expected {}, but counted {}.".format(Game.VALID_NUM_RESOURCES, num_tiles))

        if len(duplicate_check) != Game.VALID_NUM_RESOURCES:
            self.require_tile_num = True
            duplicate_tiles = ""
            for tile in possible_duplicate_tiles:
                if possible_duplicate_tiles[tile] > 1:
                    duplicate_tiles += tile + " "
            print("\nMultiple tiles found: {t}".format(t=duplicate_tiles))
            print("Please specify tile number when calling tile specific commands.\n")

        if DEBUG:
            print("create_board, board: {}".format(self.board))

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
            if DEBUG:
                print(new_player)
        return

    def roll(self, dice):
        for player in self.players:
            player.cards_roll_resource(dice, self.robber)
        return

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
        return

    def player_robs(self, player1, player2, tile):
        curr_player = self.resolve_player(player1)
        robbed_player = self.resolve_player(player2)
        curr_player.cards_rob_resource(robbed_player)
        return

    def player_trades(self, player1, resources1, player2, resources2):
        curr_player1 = self.resolve_player(player1)
        curr_player2 = self.resolve_player(player2)

        curr_player1.cards_update_resource(resources1, award=False)
        curr_player1.cards_update_resource(resources2, award=True)

        curr_player2.cards_update_resource(resources2, award=False)
        curr_player2.cards_update_resource(resources1, award=True)
        return

    def game_players(self):
        for player in self.players:
            print("P{order}-{name}".format(order=player.order, name=player.name))
        return

    def game_player_name(self, player, name):
        self.resolve_player(player).name = name
        return

    def game_cards(self):
        for player in self.players:
            print(player)
        return

    def game_fix(self, player, cards):
        curr_player = self.resolve_player(player)
        for card in cards:
            if card not in Game.VALID_RESOURCE_NAME:
                raise Exception("Invalid card value {c}.".format(c=card))
            curr_player.hand[card] += 1
        return

    def game_clear_cards(self, player):
        curr_player = self.resolve_player(player)
        for resource in curr_player.hand:
            curr_player.hand[resource] = 0
        return

    def game_board(self):
        board_str = ""
        split = [2, 6, 11, 15, 18]
        for i, tile in enumerate(self.board_tiles):
            board_str += str(tile) 

            if i in split:
                print()
                print(board_str.center(50))
                board_str = ""
            else:
                board_str += ", "

        print()
        return 