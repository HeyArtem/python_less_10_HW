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

        game_foll_unitest = Deck() # создали колоду game_foll_unitest -> колода версия 1
        cards_before = game_foll_unitest.cards[:] # создали перемннную cards_before которая равна колода версия 1 (сохранение последовательности добиваемя срезом)
        swich = False # создали переменную Ложь
        game_foll_unitest.shuffle() # тасуем колоду
        cards_after = game_foll_unitest.cards # создали пременную которой присвоено перетасованная колоду версии 1, теперь это колода -> Версия 2
        for i,j in zip(cards_before, cards_after): # сравниваем по позициям колоды Версия 1 и версия 2 если есть расхождения, то переменной sich присваиватся True
            if i != j:
                swich = True
            self.assertEqual(True, swich) # Спавниваем два значения True и swich (тоже будет True, если карты перетасованы)





if __name__ == '__main__':
    unittest.main()
