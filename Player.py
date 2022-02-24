class Player:

    def __init__(self, name="No Name", order=None):

        self.hand = {"w":0, "b":0, "s":0, "t":0, "o":0, "u":0} 

        self.name = name
        self.order = order

        self.settlements = {}
        self.num_settlements = 0
        
        self.cities = {}
        self.num_cities = 0

    def cards_roll_resource(self, roll, robber):

        print(roll, self.settlements)

        if roll in self.settlements:
            for resource in self.settlements[roll]:
                if robber.tile != str.join(roll, resource):
                    self.hand[resource] += 1

        if roll in self.cities:
            for resource in this.cities[roll]:
                if robber.tile != str.join(roll, resource):
                    self.hand[resource] += 2

        return

    def cards_rob_resource(self, player):
        pass

    def use_cards(self, purpose, tiles=None):

        if purpose == "settlement":
            self.cards_build_settlement()
            self.tiles_build_settlement(tiles)
        elif purpose == "city":
            self.cards_build_city()
            self.tiles_build_city(tiles)
        elif purpose == "road":
            self.cards_build_road()
        elif purpose == "dev":
            self.cards_buy_dev()

    def cards_build_settlement(self):

        # Don't remove cards for the first two settlments
        if self.num_settlements + self.num_cities < 2:
            return
        self.num_settlements += 1
        
        self.hand["w"] -= 1
        self.hand["b"] -= 1
        self.hand["s"] -= 1
        self.hand["t"] -= 1

    def cards_build_city(self):
        self.num_settlements -= 1
        self.num_cities += 1
        
        self.hand["t"] -= 2
        self.hand["o"] -= 3

    def cards_build_road(self):
        self.hand["b"] -= 1
        self.hand["w"] -= 1      

    def cards_buy_dev(self):
        self.hand["s"] -= 1
        self.hand["t"] -= 1
        self.hand["o"] -= 1

    def cards_update_resource(self, resources, award=True):

        if award:
            update = 1
        else:
            update = -1
        
        for res in resources:
            self.hand[res] += update

    def tiles_build_settlement(self, tiles):
        for t in tiles:
            if t.frequency not in self.settlements:
                 self.settlements[t.frequency] = []
            self.settlements[t.frequency] += t.resource

    def tiles_build_city(self, tiles):
        for t in tiles:
            if t.frequency not in self.settlements:
                raise Exception("Invalid City Placement. No settlement to upgrade to city at tiles {}".format(tiles.join(',')))
            
            self.settlements[t.frequency].remove(t.resource)
            
            if t.frequency not in self.cities:
                self.cities[t.frequency] = []
            self.cities[t.frequency] += t.resource


    def __str__(self):

        cards_str = ""
        for resource in self.hand:
            cards_str += "{res}:{num_res} ".format(res=resource, num_res=self.hand[resource])
        
        return "P{order}-{name} Hand: {cards_in_hand}".format(order=self.order, name=self.name, cards_in_hand=cards_str)

    def __eq__(self):
        pass