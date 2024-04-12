import pygame
import os

# Set up the environment for Pygame to use a specific audio driver
os.environ['SDL_AUDIODRIVER'] = 'dsp'

pygame.init()
pygame.display.set_caption('Kidney Stone Simulator')
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
target_fps = 60

# Game settings/constants
stoneCount = 0
stonePerClick = 1
stonePerSecond = 0
totalUserMulti = 1

# Debugging settings
debugAutoClickerEnabled = True
debugAutoClickerSlider = 1000

# Player input
currentPerson = input("Enter your name: ")
peopleToUnlock = [
    currentPerson, "Mazen Ibrahim", "Barry Smith", "Pedro Martinez", "Andrew Ginther", "William Shatner",
    "Lil Nas X", "Travis Scott", "Lebron James", "Dwayne Johnson", "Taylor Swift", "Lionel Messi", "Cristiano Ronaldo"
]

costOfPeople = [100, 1000, 5000, 25000, 66000, 175000, 375000, 1000000, 3505000, 8000000, 15000000, 30050000, 59000000]
costIncreaseFactor = [1.5] * len(costOfPeople)
basePeopleValues = [1, 2, 5, 10, 25, 50, 100, 250, 500, 1000, 3500, 6000, 10000]

additional = 0

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
            if screen_width / 2 - 100 <= mouse_pos[0] <= screen_width / 2 + 100 and screen_height / 2 - 100 <= mouse_pos[1] <= screen_height / 2 + 100:
                stoneCount = clickedStone(stoneCount, stonePerClick, totalUserMulti, additional)
            elif screen_width - 210 <= mouse_pos[0] <= screen_width and 10 <= mouse_pos[1] <= 10 + 60 * len(peopleToUnlock):
                for i in range(len(peopleToUnlock)):
                    if 10 + 60 * i <= mouse_pos[1] <= 10 + 60 * (i + 1):
                        if stoneCount >= costOfPeople[i]:
                            stoneCount -= costOfPeople[i]
                            totalUserMulti += basePeopleValues[i]
                            costOfPeople[i] *= costIncreaseFactor[i]  # Increase the cost
                            print(f"Unlocked {peopleToUnlock[i]}")
                            break
        # Debug auto clicker functionality
    if debugAutoClickerEnabled:
        for _ in range(debugAutoClickerSlider):
            stoneCount = clickedStone(stoneCount, stonePerClick, totalUserMulti, additional)

    screen.fill("white")
    for i in range(len(peopleToUnlock)):
        person_rect = pygame.draw.rect(screen, "#cca933", (screen_width - 310, 10 + 60 * i, 200, 60))

        # Check if the cost is larger than a certain threshold
        if costOfPeople[i] > 1000000:  # Adjust this value as needed
            # If it is, display it in scientific notation
            cost_text = "{:.2e}".format(costOfPeople[i])
        else:
            # If it's not, display it normally
            cost_text = str(costOfPeople[i])

        person_text = font.render(f"{peopleToUnlock[i]} Cost: {cost_text}", True, (0, 0, 0))
        screen.blit(person_text, person_rect)

    stone_rect = pygame.draw.rect(screen, "#cca933", (screen_width / 2 - 100, screen_height / 2 - 100, 200, 200))
    stone_text = font.render(f"Stones: {stoneCount}", True, (0, 0, 0))
    screen.blit(stone_text, stone_rect.topleft)
    current_player_text = font.render(f"You are {currentPerson}", True, (0, 0, 0))
    screen.blit(current_player_text, (10, 30))

    pygame.display.flip()
    clock.tick(target_fps)

pygame.quit()
