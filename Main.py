import sys
import pygame
import os

os.environ['SDL_AUDIODRIVER'] = 'dsp'
pygame.init()
pygame.display.set_caption('Kidney Stone Simulator')
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
target_fps = 60

# Game settings/constants
stoneCount = 0
stonePerClick = 1
stonePerSecond = 0
totalUserMulti = 1

# for plus 5 per click or something

additional = 0
currentPerson = input("Enter your name: ")
peopleToUnlock = [
    currentPerson,
    "Mazen Ibrahim",
    "Barry Smith",
    "Pedro Martinez",
    "Andrew Ginther",
    "William Shatner",
    "Lil Nas X",
    "Travis Scott",
    "Lebron James",
    "Dwayne Johnson",
    "Taylor Swift",
    "Lionel Messi",
    "Cristiano Ronaldo"
]

costOfPeople = [
    1,
    7,
    200,
    700,

]


def clickedStone(stoneCount, stonePerClick, totalUserMulti, additional):
    added = stonePerClick * totalUserMulti + additional
    stoneCount += added
    return stoneCount


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if screen_width / 2 - 100 <= mouse_pos[0] <= screen_width / 2 + 100 and screen_height / 2 - 100 <= \
                    mouse_pos[1] <= screen_height / 2 + 100:
                stoneCount = clickedStone(stoneCount, stonePerClick, totalUserMulti, additional)

    screen.fill("white")
    pygame.draw.rect(screen, ("#cca933"), (screen_width / 2 - 100, screen_height / 2 - 100, 200, 200))
    stoneCountText = font.render(f"Stones: {stoneCount}", True, (0, 0, 0))
    currentPlayerText = font.render(f"You are {currentPerson}", True, (0, 0, 0))
    screen.blit(stoneCountText, (10, 10))
    screen.blit(currentPlayerText, (10, 30))

    pygame.draw.rect(screen, ("#cca933"), (screen_width / 2 - 100, screen_height / 2 - 100, 150, 100))

    pygame.display.flip()
    clock.tick(target_fps)

pygame.quit()



