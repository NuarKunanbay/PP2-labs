import pygame
import random
import sys
import psycopg2
import json

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Frame rate controller
clock = pygame.time.Clock()
fps = 10

# Snake and food settings
snake_size = 10
snake_pos = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, width//snake_size) * snake_size,
            random.randrange(1, height//snake_size) * snake_size]
food_spawn = True
direction = 'RIGHT'
change_to = direction

# Connect to the database
conn = psycopg2.connect("dbname=yourdbname user=youruser password=yourpassword")
cur = conn.cursor()

def save_game_state(snake_pos, score):
    user_id = get_or_create_user("your_username_here")  # Adjust as needed
    game_state = {
        "snake_position": snake_pos,
        "score": score
    }
    cur.execute("""
        INSERT INTO user_scores (user_id, score, game_state)
        VALUES (%s, %s, %s)
        ON CONFLICT (user_id) DO UPDATE
        SET score = EXCLUDED.score, game_state = EXCLUDED.game_state
    """, (user_id, score, json.dumps(game_state)))
    conn.commit()

def get_or_create_user(username):
    cur.execute("SELECT user_id FROM users WHERE username = %s", (username,))
    user_id = cur.fetchone()
    if user_id is None:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING user_id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
    return user_id

# Game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    go_surface = my_font.render('Your Score is: ' + str(len(snake_pos) - 3), True, red)
    go_rect = go_surface.get_rect()
    go_rect.midtop = (width / 2, height / 4)
    screen.fill(black)
    screen.blit(go_surface, go_rect)
    save_game_state(snake_pos, len(snake_pos) - 3)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_p:  # Pause key
                save_game_state(snake_pos, len(snake_pos) - 3)

    # Validate direction
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    elif change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    elif change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    elif change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    # Move snake
    if direction == 'RIGHT':
        snake_pos[0][0] += snake_size
    elif direction == 'LEFT':
        snake_pos[0][0] -= snake_size
    elif direction == 'UP':
        snake_pos[0][1] -= snake_size
    elif direction == 'DOWN':
        snake_pos[0][1] += snake_size

    # Snake body growing mechanism
    snake_pos.insert(0, list(snake_pos[0]))
    if snake_pos[0] == food_pos:
        score = len(snake_pos)
        food_spawn = False
    else:
        snake_pos.pop()

    # Food Spawn
    if not food_spawn:
        food_pos = [random.randrange(1, width//snake_size) * snake_size,
                    random.randrange(1, height//snake_size) * snake_size]
    food_spawn = True

    # Background and Snake/Food drawing
    screen.fill(black)
    for pos in snake_pos:
        pygame.draw.rect(screen, white, pygame.Rect(pos[0], pos[1], snake_size, snake_size))

    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], snake_size, snake_size))

    # Game Over conditions
    if snake_pos[0][0] < 0 or snake_pos[0][0] > width-snake_size:
        game_over()
    if snake_pos[0][1] < 0 or snake_pos[0][1] > height-snake_size:
        game_over()
    for block in snake_pos[1:]:
        if snake_pos[0] == block:
            game_over()

    pygame.display.update()
    clock.tick(fps)

# Clean up
cur.close()
conn.close()
