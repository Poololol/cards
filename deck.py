from card import Card
from cardGroup import CardGroup
import pygame
import utils
import random

font = pygame.font.Font(None, 36)
random.seed(1)

class Deck(CardGroup):
    def __init__(self, cards: list[Card] | None = None):
        '''
        Creates a deck of cards
        If cards is None, creates a standard deck of 52 cards
        '''
        if cards is None:
            cards = [Card(value, suit) for value in range(1, 14) for suit in range(4)]
        super().__init__(cards)
        self.originalCards = self.cards.copy()
        random.shuffle(self.cards)

    def draw(self, surface: pygame.Surface, pos: tuple[float, float], size: tuple[float, float], num: bool = False) -> None:
        '''
        Draws the deck of cards
        '''
        super().draw(surface, pos, size, style='Stack', direction='Up', face='Down', spacing=.33)
        if num:
            self.drawNumCards(surface, (pos[0] + size[0]/2, pos[1] + size[1]), size)

    def drawNumCards(self, surface: pygame.Surface, pos: tuple[float, float], size: tuple[float, float]) -> None:
        '''
        Draws the number of cards in the deck
        Pos is the top-center of the text
        '''
        text = font.render(f'{len(self.cards)}/{len(self.originalCards)}', True, utils.black)
        surface.blit(text, (pos[0] - text.get_width()/2, pos[1]))
        

    def deal(self, num: int, hand: CardGroup | None = None) -> list[Card]:
        '''
        Deals a number of cards from the deck
        '''
        if hand is not None:
            hand.addCards(self.cards[-num:])
        return [self.cards.pop() for _ in range(num)]
    
    def shuffle(self) -> None:
        '''
        Shuffles the deck
        '''
        random.shuffle(self.cards)