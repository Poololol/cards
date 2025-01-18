import pygame
import utils
from typing import Literal

font = pygame.font.Font(None, 36)

class Card():
    highContrast = False

    def __init__(self, value: int, suit: int) -> None:
        self.value = value
        self.suit = suit
        self.label = str(value) if value <= 10 else ['J', 'Q', 'K', 'A'][value - 11]
        self.color = (utils.red if suit in [0, 1] else utils.black) if not self.highContrast else [utils.red, utils.orange, utils.lightBlue, utils.black][suit]
    
    def draw(self, screen: pygame.Surface, pos: tuple[float, float], size: tuple[float, float], face: Literal['Up', 'Down'] = 'Up') -> None:
        #pygame.draw.rect(screen, utils.gray, (*pos, 100, 150))
        pos2 = utils.Coordinate(xy=pos)
        size2 = utils.Coordinate(xy=size)
        utils.DrawRoundedRect(screen, utils.darkWhite, (pos2.xy, size2.xy), 5, 0)
        utils.DrawRoundedRect(screen, utils.lightGray, (pos2.xy, size2.xy), 5, 1)
        #utils.DrawRoundedRect(screen, self.color, (*pos, 100, 150), 25, 3)
        #pygame.draw.rect(screen, self.color, (*(utils.Coordinate(5,5)+pos).xy, 100-10, 150-10), 5)
        if face ==  'Up':
            text = font.render(self.label, True, self.color)
            screen.blit(text, (pos[0] + 5, pos[1] + 5))
            text = font.render(self.label, True, self.color)
            screen.blit(text, (pos[0] + size[0] - 5 - text.get_width(), pos[1] + size[1] - 5 - text.get_height()))
    
    def drawCards(screen: pygame.Surface, cards: list['Card'], pos: tuple[float, float], size: tuple[float, float], style: Literal['Stack', 'Overlap', 'Separate'] = 'Separate', direction: Literal['Up', 'Down', 'Left', 'Right'] = 'Right', face: Literal['Up', 'Down'] = 'Up', spacing: float = 5):
        direct = {'Up': 0, 'Down': 1, 'Left': 2, 'Right': 3}[direction]
        pos = utils.Coordinate(xy=pos)
        size = utils.Coordinate(xy=size)
        if style == 'Stack':
            if direct%2 == 0:
                cards[-1].draw(screen, pos, size, face)
            else:
                cards[0].draw(screen, pos, size, face)
        elif style == 'Overlap':
            if direct <= 1:
                sign = 2*direct - 1
                for i in range(len(cards)):
                    cards[i].draw(screen, (pos + (0, sign*spacing*i)), size, face)
            else:
                sign = 2*direct - 5
                for i in range(len(cards)):
                    cards[i].draw(screen, (pos + (sign*spacing*i, 0)), size, face)
        else:
            if direct <= 1:
                sign = 2*direct - 1
                for i in range(len(cards)):
                    cards[i].draw(screen, (pos + (0, sign*i*(spacing+size[1]))), size, face)
            else:
                sign = 2*direct - 5
                for i in range(len(cards)):
                    cards[i].draw(screen, (pos + (sign*i*(spacing+size[0]), 0)), size, face)
        
    def setHighContrast(highContrast: bool) -> None:
        Card.highContrast = highContrast

    def __str__(self) -> str:
        return f'{self.label} of {["Hearts", "Diamonds", "Clubs", "Spades"][self.suit]}'
    
class CardGroup():
    def __init__(self, cards: list[Card]):
        self.cards = cards
    
    def draw(self, screen: pygame.Surface, pos: tuple[float, float], size: tuple[float, float], style: Literal['Stack', 'Overlap', 'Separate'] = 'Separate', direction: Literal['Up', 'Down', 'Left', 'Right'] = 'Right', face: Literal['Up', 'Down'] = 'Up', spacing: float = 5):
        Card.drawCards(screen, self.cards, pos, size, style, direction, face, spacing)