import pygame
import utils
from typing import Literal
from card import Card

font = pygame.font.Font(None, 36)

def suitSort(card: Card) -> tuple[int, int]:
    if card.suit == 0:
        return 0, 14 - card.value
    elif card.suit == 1:
        return 2, 14 - card.value
    elif card.suit == 2:
        return 1, 14 - card.value
    else:
        return 3, 14 - card.value

class CardGroup():
    def __init__(self, cards: list[Card] = [], maxSelected: int = -1) -> None:
        self.cards = cards
        self.cardsReversed = cards[::-1]
        self.maxSelected = maxSelected
        self.selectedCards = [False]*len(cards)
    
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
        self.screen = screen
        Card.drawCards(screen, self.cards, pos, size, style, direction, face, spacing)
    
    def processEvent(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for card in self.cardsReversed:
                if card.rect.collidepoint(event.pos):
                    #card.processEvent(event)
                    if card.raised:
                        card.raised = False
                        self.selectedCards[self.cards.index(card)] = False
                    elif (self.selectedCards.count(True) < self.maxSelected or self.maxSelected == -1):
                        card.raised = True
                        self.selectedCards[self.cards.index(card)] = True
                    break

    def processMouse(self, pos: tuple[float, float], pressed: tuple[bool, bool, bool]):
        for card in self.cardsReversed:
            if card.rect.collidepoint(pos):
                #card.processMouse(pos, pressed)
                card.drawTooltip(self.screen, 'Top')
                break

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
            self.cards.sort(key=suitSort)
        else:
            self.cards.sort(key=lambda card: (card.value, card.suit), reverse=True)
        self.cardsReversed = self.cards[::-1]

    def addCard(self, card: Card) -> None:
        self.cards.append(card)
        self.cardsReversed.insert(0, card)
        self.selectedCards.append(False)
    
    def removeCard(self, card: Card) -> None:
        self.cards.remove(card)
        self.cardsReversed = self.cards[::-1]
        self.selectedCards.pop(self.cards.index(card))

    def addCards(self, cards: list[Card]) -> None: 
        for card in cards:
            self.addCard(card)

    def removeCards(self, cards: list[Card]) -> None:
        for card in cards:
            self.removeCard(card)
    
    def __len__(self) -> int:
        return len(self.cards)

    def __getitem__(self, key: int) -> Card:
        return self.cards[key]

    def __setitem__(self, key: int, value: Card) -> None:
        self.cards[key] = value