from card import Card
from cardGroup import CardGroup
import pygame
import utils
import random

class Deck(CardGroup):
    def __init__(self, cards: list[Card] | None = None):
        '''
        Creates a deck of cards
        If cards is None, creates a standard deck of 52 cards
        '''
        if cards is None:
            cards = [Card(value, suit) for value in range(1, 14) for suit in range(4)]
        super().__init__(cards)
        random.shuffle(self.cards)

    def draw(self, surface: pygame.Surface, pos: tuple[float, float], size: tuple[float, float]) -> None:
        '''
        Draws the deck of cards
        '''
        super().draw(surface, pos, size, style='Stack', direction='Up', face='Down', spacing=.33)

    def deal(self, num: int) -> list[Card]:
        '''
        Deals a number of cards from the deck
        '''
        return [self.cards.pop() for _ in range(num)]
    
    def shuffle(self) -> None:
        '''
        Shuffles the deck
        '''
        random.shuffle(self.cards)