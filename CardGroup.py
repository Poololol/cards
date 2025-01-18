import pygame
import utils
from typing import Literal
from card import Card

font = pygame.font.Font(None, 36)

class CardGroup():
    def __init__(self, cards: list[Card]):
        self.cards = cards
    
    def draw(self, screen: pygame.Surface, pos: tuple[float, float], size: tuple[float, float], 
             style: Literal['Stack', 'Overlap', 'Separate'] = 'Separate',
             direction: Literal['Up', 'Down', 'Left', 'Right'] = 'Right', 
             face: Literal['Up', 'Down'] = 'Up', spacing: float = 5) -> None:
        Card.drawCards(screen, self.cards, pos, size, style, direction, face, spacing)
    
    def getPokerHand(self) -> str:
        if self.isFlush() and self.isStraight():
            return 'Straight Flush'
        if self.isXOfAKind(4):
            return 'Four of a Kind'
        if self.isXOfAKind(3) and self.isXOfAKind(2):
            return 'Full House'
        if self.isFlush():
            return 'Flush'
        if self.isStraight():
            return 'Straight'
        if self.isXOfAKind(3):
            return 'Three of a Kind'
        if self.isXOfAKind(2):
            if sum(1 for card in self.cards if card.value == 11) == 2:
                return 'Two Pair'
            return 'One Pair'
        return 'High Card'

    def isFlush(self) -> bool:
        suits = [card.suit for card in self.cards]
        return len(set(suits)) == 1
    
    def isStraight(self, length: int = 5) -> bool:
        values = [card.value for card in self.cards]
        values.sort()
        return values == list(range(values[0], values[0] + length))

    def isXOfAKind(self, x: int) -> bool:
        values = [card.value for card in self.cards]
        return any(values.count(value) == x for value in values)

    def addCard(self, card: Card) -> None:
        self.cards.append(card)
    
    def removeCard(self, card: Card) -> None:
        self.cards.remove(card)
    
    def __len__(self) -> int:
        return len(self.cards)

    def __getitem__(self, key: int) -> Card:
        return self.cards[key]

    def __setitem__(self, key: int, value: Card) -> None:
        self.cards[key] = value