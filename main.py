import pygame
import utils
from card import Card
from cardGroup import CardGroup
from deck import Deck

clock = pygame.time.Clock()
screen = pygame.display.set_mode((701, 501), pygame.RESIZABLE)
screenSize = screen.get_size()

def main():
    Card.highContrast =  True
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
    hand = CardGroup(maxSelected=5)
    hand.addCards(deck.deal(15))
    hand.sort('Rank')

    sortRank = utils.Setting.Button(utils.orange, utils.lightRed, utils.white, utils.white, 'Rank')
    sortSuit = utils.Setting.Button(utils.orange, utils.lightRed, utils.white, utils.white, 'Suit')

    print(f'Hand is a {cards.getPokerHand()}')
    while True:
        screenSize = screen.get_size()
        screen.fill(utils.darkGreen)
        mousePos = pygame.mouse.get_pos()
        
        cards.draw(screen, pos=(10, 10), size=cardSize, style='Separate', face='Down')
        deck.draw(screen, pos=(10, 150), size=cardSize, num=True)
        hand.draw(screen, pos=(10, 300), size=cardSize, spacing=cardWidth/1.5)
        
        sortRank.Render(screen, (screenSize[0]/2 - 20, screenSize[1] - 20), 20, mousePos)
        sortSuit.Render(screen, (screenSize[0]/2 + 20, screenSize[1] - 20), 20, mousePos)

        hand.processMouse(mousePos, pygame.mouse.get_pressed())
        for event in pygame.event.get():
            hand.processEvent(event)
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if sortRank.Clicked(event):
                    hand.sort('Rank')
                elif sortSuit.Clicked(event):
                    hand.sort('Suit')
        
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()