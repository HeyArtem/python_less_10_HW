import unittest
from game_fool import Card
from game_fool import Deck

class Test_game_fool(unittest.TestCase):

    def test_1_fool_init(self):
        '''
        Тест1
        Создал карту с мастью (suit)=2
        и достоинством (rank)=3
        Здесь сравниваю suit
        '''
        game_foll_unitest = Card(2,3)
        self.assertEqual(2, game_foll_unitest.suit)

    def test_2_fool_rank(self):
        '''
        Тест 2
        Создал карту с мастью (suit)=2
        и достоинством (rank)=3
        Здесь сравниваю rank
        '''
        game_foll_unitest = Card(2, 3)
        self.assertEqual(3, game_foll_unitest.rank)

    def test_3_fool_str(self):
        '''
        Тест 3
        Тестирую строчное представление карты
        Создал карту Card(2(масть-Черви), 3(ранк-8))
        '''
        game_foll_unitest = Card(2, 3)
        self.assertEqual('8 of Черви ♡', str(game_foll_unitest))

    def test_4_fool_init_Deck(self):
        '''
        Тест 4
        Тестирую количество карт в созданной колоде
        Их должно быть 36
        '''
        game_foll_unitest = Deck()
        self.assertEqual(36, (len(game_foll_unitest.cards)))

    def test_5_fool_init_shuffle(self):
        '''
        Тест 5
        Тестирую метод shuffle
        тасую карты в колоде
        '''
        game_foll_unitest = Deck()
        peremen = game_foll_unitest.cards
        peremen_2 = False
        game_foll_unitest.shuffle()
        peremen_3 = game_foll_unitest.cards

        for i, j in zip(peremen, peremen_3):
            if i != j:
                peremen_2 = True
        self.assertEqual(False, peremen_2)




if __name__ == '__main__':
    unittest.main()
