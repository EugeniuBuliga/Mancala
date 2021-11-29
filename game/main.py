import sys, pygame

from game.options import *

pygame.init()

size = WIDTH, HEIGHT
WIN = pygame.display.set_mode(size)
pygame.display.set_caption("Salam")


def set_text(string, x, y):
    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render(string, True, (0,0,0))
    textRect = text.get_rect()
    textRect.center = (x,y)
    return (text, textRect)


if __name__ == '__main__':
    clock = pygame.time.Clock()
    i = 0
    h= HEIGHT
    w=WIDTH
    run = True
    while run:
        RAND_COLOR = (rand.randint(1, 255), rand.randint(1, 255), rand.randint(1, 255))
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                i+=1
                pygame.draw.rect(WIN,RAND_COLOR,(i,i,w-2*i,h-2*i))
                ttext = set_text(str(i),w/2,h/2)
                WIN.blit(ttext[0],ttext[1])



        pygame.display.update()
    pygame.quit()
