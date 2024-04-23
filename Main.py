import pygame
import math
import os

os.environ['SDL_AUDIODRIVER'] = 'dsp'

pygame.init()
pygame.display.set_caption('Kidney Stone Simulator')
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
target_fps = 60

stone_count = 0
stone_per_click = 1
stone_per_second = 0
total_user_multiplier = 1

debug_auto_clicker_enabled = False
debug_auto_clicker_speed = 1000

format_type = "short"
click_type = "single"
kevin_mode = False

current_person = input("Enter your name: ")
people_to_unlock = [
    current_person, "Mazen Ibrahim", "Barry Smith", "Pedro Martinez", "Andrew Ginther", "William Shatner",
    "Lil Nas X", "Travis Scott", "Lebron James", "Dwayne Johnson", "Taylor Swift", "Lionel Messi", "Cristiano Ronaldo"
]

cost_of_people = [100, 1000, 5000, 25000, 66000, 175000, 375000, 1000000, 3505000, 8000000, 15000000, 30050000, 59000000]
cost_increase_factor = [1.5] * len(cost_of_people)
base_people_values = [1, 2, 5, 10, 25, 50, 100, 250, 500, 1000, 3500, 6000, 10000]

illions = [
    "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion",
    "septillion", "octillion", "nonillion", "decillion", "undecillion", "duodecillion",
    "tredecillion", "quattuordecillion", "quindecillion", "sexdecillion", "septendecillion",
    "octadecillion", "novemdecillion", "vigintillion", "unvigintillion", "duovigintillion",
    "trevigintillion", "quattuorvigintillion", "quinvigintillion", "sexvigintillion",
    "septenvigintillion", "octavigintillion", "novemvigintillion", "trigintillion",
    "untrigintillion", "duotrigintillion"
]

def clicked_stone(click_type="single"):
    global stone_count
    if click_type == "single":
        added = stone_per_click * total_user_multiplier
    elif click_type == "hacker":
        added = 10 * stone_per_click * total_user_multiplier
    else:
        return
    stone_count += added
    return stone_count


def get_item_in_list(list, index):
    try:
        return list[index]
    except IndexError:
        return None



def format_cost(cost, format_type):
    if cost > 1000000:
        exponent = int(math.log10(cost) // 3) * 3
        base = cost / 10**exponent
        if format_type == "short":
            return f"{base:.2f}{illions[(exponent//3)-2][0].upper()}"
        elif format_type == "long":
            return f"{base:.2f} {illions[(exponent//3)-2]}"
    return str(cost)

def display_costs(format_type="short"):
    for i, person in enumerate(people_to_unlock):
        person_rect = pygame.draw.rect(screen, "#cca933", (screen_width - 1900, 80 + 60 * i, 200, 60))
        cost = get_item_in_list(cost_of_people, i)
        cost_text = f"{person} Cost: {format_cost(cost, format_type)}"
        person_text = font.render(cost_text, True, (0, 0, 0))
        screen.blit(person_text, person_rect)

def display_stone_count(format_type="short"):
    screen.fill("white")
    stone_text = font.render(f"Stones: {format_cost(stone_count, format_type)}", True, (0, 0, 0))
    stone_rect = pygame.draw.rect(screen, "#cca933", (screen_width / 2 - 100, screen_height / 2 - 100, 200, 50))
    screen.blit(stone_text, (stone_rect.x + 10, stone_rect.y + 10))
    display_costs(format_type)


def format_stones(count):
    if count >= 1000000:
        exponent = int(math.log10(count) // 3) * 3
        base = count / 10**exponent
        return f"{base:.2f} {illions[(exponent//3)-2]}"
    return str(count)


def draw_format_button():
    button_color = "#cca933"
    button_rect = pygame.draw.rect(screen, button_color, (screen_width - 200, 10, 180, 60))
    button_text = font.render(f"Format: {format_type}", True, (0, 0, 0))
    screen.blit(button_text, button_rect)


def check_format_button_click(mouse_pos):
    global format_type
    if screen_width - 200 <= mouse_pos[0] <= screen_width - 20 and 10 <= mouse_pos[1] <= 70:
        if format_type == "short":
            format_type = "long"
        else:
            format_type = "short"


def draw_kevin_button():
    button_color = "#cca933"
    button_rect = pygame.draw.rect(screen, button_color, (screen_width - 200, 80, 180, 60))
    button_text = font.render("Kevin Mode: ON" if kevin_mode else "Kevin Mode: OFF", True, (0, 0, 0))
    screen.blit(button_text, button_rect)

def check_kevin_button_click(mouse_pos):
    global kevin_mode
    global click_type
    if screen_width - 200 <= mouse_pos[0] <= screen_width - 20 and 80 <= mouse_pos[1] <= 140:
        if not kevin_mode:
            password = input("Enter password: ")
            if password == "please give me a 5":
                kevin_mode = True
                click_type = "hacker"
        else:
            kevin_mode = False
            click_type = "single"
    else:
        print("Try and guess the password for Kevin Mode!!!!!")

def run_game():
    global total_user_multiplier
    global stone_count
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                check_format_button_click(mouse_pos)
                check_kevin_button_click(mouse_pos)
                if screen_width / 2 - 100 <= mouse_pos[0] <= screen_width / 2 + 100 and screen_height / 2 - 100 <= mouse_pos[1] <= screen_height / 2 + 100:
                    clicked_stone(click_type)
                elif screen_width - 1900 <= mouse_pos[0] <= screen_width - 1700 and 80 <= mouse_pos[1] <= 80 + 60 * len(people_to_unlock):
                    for i in range(len(people_to_unlock)):
                        if 80 + 60 * i <= mouse_pos[1] <= 80 + 60 * (i + 1) and stone_count >= cost_of_people[i]:
                            stone_count -= cost_of_people[i]
                            total_user_multiplier += base_people_values[i]
                            cost_of_people[i] *= cost_increase_factor[i]
                            print(f"Unlocked {people_to_unlock[i]}")
                            break
        if debug_auto_clicker_enabled:
            for i in range(debug_auto_clicker_speed):
                clicked_stone(click_type)

        display_stone_count(format_type)
        current_player_text = font.render(f"You are {current_person}", True, (0, 0, 0))
        screen.blit(current_player_text, (10, 30))
        draw_format_button()
        draw_kevin_button()

        pygame.display.flip()
        clock.tick(target_fps)

    pygame.quit()

run_game()