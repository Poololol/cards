import pygame
import utils
from typing import Literal
from card import Card

font = pygame.font.Font(None, 36)

class CardGroup():
    def __init__(self, cards: list[Card] = []) -> None:
        self.cards = cards
    
    def draw(self, screen: pygame.Surface, pos: tuple[float, float], size: tuple[float, float], 
             style: Literal['Stack', 'Overlap', 'Separate'] = 'Overlap',
             direction: Literal['Up', 'Down', 'Left', 'Right'] = 'Right', 
             face: Literal['Up', 'Down'] = 'Up', spacing: float = -1, num: bool = True) -> None:
        if spacing == -1:
            if style == 'Stack':
                spacing = .5
            elif style == 'Overlap':
                spacing = size[0]/2
            else:
                spacing = 5
        Card.drawCards(screen, self.cards, pos, size, style, direction, face, spacing)
    
    def getPokerHand(self) -> str:
        if self.isFlush() and self.isStraight():
            return 'Straight Flush'
        if self.isXOfAKind(4) >= 1:
            return 'Four of a Kind'
        if self.isXOfAKind(3) >= 1 and self.isXOfAKind(2) >= 1:
            return 'Full House'
        if self.isFlush():
            return 'Flush'
        if self.isStraight():
            return 'Straight'
        if self.isXOfAKind(3) >= 1:
            return 'Three of a Kind'
        if self.isXOfAKind(2) >= 2:
            return 'Two Pair'
        if self.isXOfAKind(2) >= 1:
            return 'Pair'
        return 'High Card'

    def isFlush(self) -> bool:
        suits = [card.suit for card in self.cards]
        return len(set(suits)) == 1
    
    def isStraight(self, length: int = 5) -> bool:
        values = [card.value for card in self.cards]
        values.sort()
        return values == list(range(values[0], values[0] + length))

    def isXOfAKind(self, x: int) -> int:
        '''Returns the number of "x of a kind" in the hand'''
        values = [card.value for card in self.cards]
        #print(values, x, list(values.count(value) == x for value in values), list((values.count(value) == x for value in values)).count(True))
        #return any(values.count(value) == x for value in values)
        return list((values.count(value) == x for value in values)).count(True)/x
    
    def sort(self, method: Literal['Suit', 'Rank'] = 'Rank') -> None:
        if method == 'Suit':
            self.cards.sort(key=lambda card: (card.suit, card.value))
        else:
            self.cards.sort(key=lambda card: (card.value, card.suit), reverse=True)

    def addCards(self, card: list[Card]) -> None:
        self.cards.extend(card)
    
    def removeCard(self, card: Card) -> None:
        self.cards.remove(card)
    
    def __len__(self) -> int:
        return len(self.cards)

    def __getitem__(self, key: int) -> Card:
        return self.cards[key]

    def __setitem__(self, key: int, value: Card) -> None:
        self.cards[key] = value