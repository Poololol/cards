import pygame
import utils
from card import Card, CardGroup

clock = pygame.time.Clock()
screen = pygame.display.set_mode((501, 501), pygame.RESIZABLE)
screenSize = screen.get_size()

def main():
    Card.highContrast =  True
    card1 = Card(1, 0)
    card2 = Card(13, 1)
    card3 = Card(7, 2)
    card4 = Card(14, 3)
    cards = CardGroup([card1, card2, card3, card4])

    cardWidth = 80
    cardSize = (cardWidth, cardWidth*1.5)

    while True:
        screenSize = screen.get_size()
        screen.fill(utils.darkGreen)
        
        cards.draw(screen, (2,2), cardSize, 'Separate', 'Left', 'Up', cardWidth/1.42)
        cards.draw(screen, (2,127), cardSize, 'Separate', 'Right', 'Up', 5)
        cards.draw(screen, (2,252), cardSize, 'Overlap', 'Down', 'Up', cardWidth/2)
        cards.draw(screen, (85*4+2-85, 252), cardSize, 'Overlap', 'Left', 'Up', cardWidth/1.42)
        cards.draw(screen, (85*4+2, 375+3), cardSize, 'Separate', 'Up', 'Up', 5)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()