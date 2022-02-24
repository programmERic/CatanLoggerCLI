








class GameFlow:

    def __init__(self):
        self.game = None

    def start_game_flow(self):
        self.continue_game = True
        count = 0
        while self.continue_game:
            count += 1
            #try:
            users_input = input("{count})> ".format(count=count))
            self.process_input(users_input)
            #except:
            #    print("Invalid Input: `{}`".format(users_input))
                

    def process_input(self, user_input):
        

        cmd = user_input.lower().split(" ")

        if DEBUG:
            print("user_input: {} cmd: {}".format(user_input, cmd))

        if len(cmd) == 0:
            print("No command entered")
            return

        action = cmd[0]

        #if action not in VALID_ACTION:
        #    print("Invalid Action")

        if action in ["h", "help"]:
            self.help_menu()

        elif action in ["c", "create"]:
            if len(cmd) == 1:
                self.create_game("8t,4w,11b,10t,3b,6t,12s,5o,desert,11o,5s,9w,2w,8b,4s,10o,6s,3t,8w")
            else:
                self.create_game(cmd[1:][0])

        elif action == "roll":
            dice_num = cmd[1]
            self.game.roll(dice_num)

        # build commands
        elif action in ["road", "settlement", "city", "dev"]:
            if len(cmd) == 3:
                tiles = cmd[2]
            else:
                tiles = None

            purpose, player = cmd[:2]  
            self.game.player_builds_or_buys_dev(player=player, purpose=purpose, tiles=tiles)
            
        # Game Commands
        elif action == "players":
            self.game.game_players()
        elif action == "player":
            player, name = cmd[1:3]
            self.game.game_player_name(player, name) 
        elif action == "cards":
            self.game.game_cards()
        elif action == "fix":
            selfgame.game_fix()
        elif action == "board":
            self.game.game_board()
            


        elif action in ["q", "quit"]:
            self.continue_game = False


    def create_game(self, board):
        
        if self.game != None:
            pass

        self.game = Game()
        self.game.create_board(board)
        self.game.add_players()
        

    def handle_cards():
        pass

    def help_menu(self):
        help_msg =\
        '''
        FORMAT
        <player>: the players identifer ex. defaults are p1, p2, p3, p4
        <tile>: 2/3 letters representing ex. 11s is 11 sheep tile, 3t is 3 wheat tile
        <resource>: 1 letter is 1 resource ex. bbb is 3 brick

        resource names:
         w = wood
         b = brick
         s = sheep
         t = wheaT
         o = ore
        
        COMMANDS
        
        roll COMMANDS
        -- roll <dice number>
        
        build COMMANDS
        -- road <player>
        -- settlement <player> tile1,tile2,tile3
        -- city <player> tile1,tile2,tile3
        
        robber COMMANDS
        -- robber <player1> robs <player2> <tile>

        development card COMMANDS
        -- dev <player> buy 'buys a dev card'
        -- plenty <player> <resource><resource> 'plays a year of plenty (draw two cards)'
        -- mono <player> <resource> 'plays a monopoly, gets all resource cards'
        -- knight <player1> <player2> <tile>
        -- roadbuild <player> 'plays a road building card'
        -- vp <player>
        

        trade COMMANDS
        -- trade <player> <resources> <player> <resources>

        port COMMANDS
        -- port <player> <resources to port> to <resources to gain>

        game COMMANDS
        -- players 'prints the players and their names'
        -- player <player> <name>
        -- cards 'prints the players and their cards'
        -- fix <player> <cards> 'changes the player's card totals'
        -- board 'prints the board'
        
        '''
        print(help_msg)



    def trade(self):
        pass

    def build(self):
        pass

    def cards(self):
        for player in self.players:
            print(player)


def test_input():
    return "8t,4w,11b,10t,3b,6t,12s,5o,desert,11o,5s,9w,2w,8b,4s,10o,6s,3t,8w"

    return "8t,4w,11b,\
            10t,3b,6t,12s,\
            5o,desert,11o,5s,9w,\
            2w,8b,4s,10o,\
            6s,3t,8w"


DEBUG = True

if __name__ == "__main__":


    print(test_input())
    
    gf = GameFlow()
    gf.start_game_flow()







    
