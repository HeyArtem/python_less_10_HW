import unittest
from game_fool import Card
from game_fool import Deck

class Test_game_fool(unittest.TestCase):

    def test_fool_init(self):
        '''Тест1. '''
        game_foll_unitest = Card(2,3)
        # game_foll_unitest.self.suit = 2
        self.assertEqual(2, game_foll_unitest.suit)

    def test_fool_rank(self):
        game_foll_unitest = Card(2, 3)
        self.assertEqual(3, game_foll_unitest.rank)

    def test_fool_str(self):
        game_foll_unitest = Card(2, 3)
        # self.assertEqual('8 of Черви ♡', game_foll_unitest.__str__())
        self.assertEqual('8 of Черви ♡', str(game_foll_unitest))

    def test_fool_init_Deck(self):
        game_foll_unitest = Deck()
        self.assertEqual(36, (len(game_foll_unitest.cards)))

    def test_fool_init_shuffle(self):
        game_foll_unitest = Deck()
        peremen = game_foll_unitest.cards
        peremen_2 = False
        game_foll_unitest.shuffle()
        peremen_3 = game_foll_unitest.cards

        for i, j in zip(peremen, peremen_3):
            if i != j:
                peremen_2 = True
        self.assertEqual(True, peremen_2)

# возможно не работает шафл


if __name__ == '__main__':
    unittest.main()
