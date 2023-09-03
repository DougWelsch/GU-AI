import pygame as pg
import time
import random

# Font
pg.font.init()
FONT = pg.font.SysFont("impact", 30)

# Window
WIDTH, HEIGHT = 800, 600
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Super Bash Sisters")

# Background
BG_BASE = pg.image.load("./assets/cosmos.jpg")
BG = pg.transform.grayscale(pg.transform.scale(BG_BASE, (WIDTH, HEIGHT)))

# Entity parameters
START_X, START_Y = 100, HEIGHT - 100
PLAYER_WIDTH, PLAYER_HEIGHT = 40, 40

MAX_SPEED = 10
SPEED_INC = 1

OFFSET = PLAYER_WIDTH

# Static parameters
platform = pg.Rect(3 * PLAYER_WIDTH, START_Y + PLAYER_WIDTH, WIDTH - 6 * PLAYER_WIDTH, 10)

def draw(player, cpu, elapsed_time):
    WIN.blit(BG, (0, 0))
    
    # Platform
    pg.draw.rect(WIN, "magenta", platform)
    
    # Entities
    pg.draw.rect(WIN, "green", player)
    pg.draw.rect(WIN, "red", cpu)
    
    # HUD
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (WIDTH / 2 - time_text.get_width() / 2, 10))
    
    pg.display.update()

def main():
    run = True
    PLAYER_VEL_X = 3
    PLAYER_VEL_Y = 0
    
    player = pg.Rect(START_X + OFFSET, START_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
    cpu = pg.Rect(WIDTH - START_X - PLAYER_WIDTH - OFFSET, START_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    clock = pg.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    
    while run:
        clock.tick(60)
        elapsed_time = time.time() - start_time
        
        # Handle game close
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break
            
        # Handle key presses
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            # PLAYER_VEL_X = min(PLAYER_VEL_X + 2, MAX_SPEED)
            player.x += PLAYER_VEL_X
        if keys[pg.K_LEFT]:
            # PLAYER_VEL_X = max(PLAYER_VEL_X - 2, -MAX_SPEED)
            player.x -= PLAYER_VEL_X
        if keys[pg.K_UP] and player.colliderect(platform):
            PLAYER_VEL_Y = -MAX_SPEED
            
        # player.x += PLAYER_VEL_X
        # if PLAYER_VEL_X != 0:
        #     PLAYER_VEL_X = PLAYER_VEL_X + 1 if (PLAYER_VEL_X < 0) else PLAYER_VEL_X - 1
        player.y += PLAYER_VEL_Y
        PLAYER_VEL_Y = PLAYER_VEL_Y + 1 if (PLAYER_VEL_Y > 0) else 0
            
        if player.y >= HEIGHT:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pg.display.update()
            pg.time.delay(4000)
            break
        
        draw(player, cpu, elapsed_time)
    pg.quit()

if __name__ == "__main__":
    main()