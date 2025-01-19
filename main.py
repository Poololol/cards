import pygame
import utils
from card import Card
from cardGroup import CardGroup
from deck import Deck

clock = pygame.time.Clock()
screen = pygame.display.set_mode((701, 501), pygame.RESIZABLE)
screenSize = screen.get_size()

def main():
    #Card.highContrast =  True
    card1 = Card(1, 0)
    card2 = Card(13, 1)
    card3 = Card(7, 2)
    card4 = Card(13, 3)
    card5 = Card(2, 2)
    cards = CardGroup([card1, card2, card3, card4, card5])

    deck = Deck()
    
    cardWidth = 80
    cardSize = (cardWidth, cardWidth*1.5)
    cards.sort('Suit')
    hand = CardGroup()
    hand.addCards(deck.deal(5))
    hand.sort('Rank')

    print(f'Hand is a {cards.getPokerHand()}')
    while True:
        screenSize = screen.get_size()
        screen.fill(utils.darkGreen)
        
        cards.draw(screen, pos=(10, 10), size=cardSize, style='Separate')
        deck.draw(screen, pos=(10, 150), size=cardSize)
        hand.draw(screen, pos=(10, 300), size=cardSize, spacing=cardWidth/1.5)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()