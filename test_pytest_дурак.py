'''
Здесь я пишу тесты pytest на игру дурак
'''

import pytest
from игра_дурак import Card

class Test_fool:

    def test_1_init(self):
        '''
        Тест 1
        Тестирую init-Инициализация карты,
        а именно suit-масть.
        В параметрах init, первое число suit(масть), второе rank(ранг)
        '''
        game_fool = Card(2, 3)
        assert game_fool.suit == 2

    def test_2_init(self):
        '''
        Тест 2
        Тестирую второй параметр-rank(ранг)
        '''
        game_fool = Card(2, 3)
        assert game_fool.rank == 3

    def test_3_str(self): #как это сдалать????????????
        ''''
        Тест 3
        Хочется протестировать строковое представление обьекта карты
        '''
        game_fool = Card(2, 3)
        assert '8 of Черви ♡'


    # def test_4_lt((self, other)): # Не получается написать тест на этот метод, не могу впихнуть в него аргументы
    #     ''''
    #     Тест 4
    #     Тестирую модуль который сравнивает карту с другими,
    #     сначала по масти, затем по рангу.
    #     возвращает: логическое (функция __lt(x < y))'''
    #     game_fool = Card(2, 3 )

    def test_4_init(self):
        ''''
        Тест 4
        Тестирую class Deck:
        конкретно метод __init__
        '''
        game_fool_Deck = Deck():



