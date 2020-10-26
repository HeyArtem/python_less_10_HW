from __future__ import print_function, division
import random


class Card:
    '''Класс стандартной игральной колоды'''

    def __init__(self, suit, rank):
        '''Инициализация карты'''
        self.suit = suit  # атрибут экз-ра класса Масть
        self.rank = rank  # атрибут экз-ра класса Достоинство(ранг)

    suit_names = ['Крести ♧', 'Буби ♢', 'Черви ♡', 'Пики ♠']
    rank_names = [None, '6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']

    def __str__(self):
        '''Строковое представление объекта карты'''
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        '''
        Сравнивает эту карту с другими, сначала по масти, затем по рангу.
        возвращает: логическое (функция __lt(x < y))
        '''
        return self.rank < other.rank and self.suit == other.suit




class Deck:
    '''Класс колоды карт'''

    def __init__(self):
        '''Инициализация колоды из 36 карт'''
        self.cards = []
        for suit in range(4):
            for rank in range(1, 10):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        '''Строковое представление объекта колоды'''
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        '''Добавление карты в колоду'''
        self.cards.append(card)

    def remove_card(self, card):
        '''Удаление карты из колоды'''
        self.cards.remove(card)

    def pop_card(self, i=-1):
        '''Возвращает вынятую из колоды карту'''
        return self.cards.pop(i)

    def shuffle(self):
        '''Перемешивает карты в колоде'''
        random.shuffle(self.cards)

    def sort(self):
        ''' Сортировка карт в порядке возрастания'''
        self.card.sort()

    def move_cards(self, hand, num):
        '''Передается num карт игроку hand'''
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    '''Колода игрока'''

    def __init__(self, label=''):
        self.cards = []
        self.label = label


deck = Deck() #создал колоду
deck.shuffle() # перетасовал
#print('Распечатываю созданную колоду deck:\n', deck) # закоментил, т.к. эта инфа мешает

artem = Hand('Artem') # Создали игрока Artem
pk = Hand ('PK') # Создали игрока PK

deck.move_cards(artem, 6) # раздал 6 карт игроку artem
deck.move_cards(pk, 6) # раздал 6 карт игроку pk

print('    Карты у игрока artem: \n', artem)
print('    Карты у игрока pk: \n', pk)
#print('    Контрольная распечатка колоды deck: \n', deck) # закоментил, т.к. эта инфа мешает

card_1 = artem.pop_card() # Этой картой ходит игрок artem
print('    Этой картой ходит игрок artem: \n', card_1)


card_2 = ""
for card in pk.cards:
    if card_1 < card:
        card_2 = pk.pop_card(pk.cards.index(card))

print('    Распечатываю карту, которой отбился PK: \n', card_2)

if card_2:
    print(f"    -> игрок {artem.label} проиграл")
else:
    print(f"     ->  игрок {pk.label} проиграл")
