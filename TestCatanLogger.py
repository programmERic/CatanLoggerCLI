import unittest
from CatanLogger import *


class TestPlayer(unittest.TestCase):

    def test_use_cards_CorrectHandAndSettlment(self):

        p = Player()
        p.hand = {"w":1, "b":1, "s":1, "t":1, "o":1}

        p.use_cards("settle", [Tile("4w"), Tile("8s"), Tile("3b")])

        self.assertEqual(p.hand, {"w":0, "b":0, "s":0, "t":0, "o":1})
        self.assertEqual(p.settlements, {3:["b"], 4:["w"], 8:["s"]})
    
    def test_use_cards_CorrectHandAndCity(self):

        p = Player()
        p.hand = {"w":1, "b":1, "s":1, "t":5, "o":5}
        p.settlements = {2:["b"], 6:["o"], 11:["s"]}


        p.use_cards("city", [Tile("11s"), Tile("2b"), Tile("6o")])

        self.assertEqual(p.hand, {"w":1, "b":1, "s":1, "t":3, "o":2})
        self.assertEqual(p.cities, {2:["b"], 6:["o"], 11:["s"]})
        self.assertEqual(p.settlements, {2:[], 6:[], 11:[]})




if __name__ == "__main__":

    unittest.main()
    






    
