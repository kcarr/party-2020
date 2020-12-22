# Import the pygame module
import pygame
import constants as const

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from player import Player
from virus import Virus
from mask import Mask
from toiletPaper import ToiletPaper

# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT))

# Create a custom event for adding a new entities
ADDVIRUS = pygame.USEREVENT + 1
pygame.time.set_timer(ADDVIRUS, 250)
ADDMASK = pygame.USEREVENT + 2
pygame.time.set_timer(ADDMASK, 1000)
ADDSCORE = pygame.USEREVENT + 3
pygame.time.set_timer(ADDSCORE, 500)
ADDTP = pygame.USEREVENT + 4
pygame.time.set_timer(ADDTP, 10000)

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Crate groups to hold virus sprites and all sprites
# - viruses is used for collision detection and position updates
# - all_sprites is used for rendering
viruses = pygame.sprite.Group()
masks = pygame.sprite.Group()
rolls = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Keep track of score
score_font = pygame.font.SysFont("monospace", 16)
mask_multiplier = 0
total_score = 0
round_score = 0
toilet_paper_score = 0
mask_counter = 0

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            
        # Did the user click the window close button? If so, stop the loop
        elif event.type == QUIT:
            running = False
    
        # Add a new virus?
        elif event.type == ADDVIRUS:
            # Create the new virus and add it to sprite groups
            new_virus = Virus()
            viruses.add(new_virus)
            all_sprites.add(new_virus)

        # Add a new mask?
        elif event.type == ADDMASK:
            # Crete the new mask and add it to sprite groups
            new_mask = Mask()
            masks.add(new_mask)
            all_sprites.add(new_mask)
        
        elif event.type == ADDTP:
            new_tp = ToiletPaper()
            rolls.add(new_tp)
            all_sprites.add(new_tp)

        elif event.type == ADDSCORE:
            round_score = round_score + 1
    
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Update positions
    masks.update()
    player.update(pressed_keys)
    viruses.update()
    rolls.update()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    
    # Draw score:
    if toilet_paper_score > 0:
        toilet_paper_text = score_font.render("OMG YOU GOT TOILET PAPER!!!!! " + str(toilet_paper_score), 1, (0, 255, 255))
        screen.blit(toilet_paper_text, (5, const.SCREEN_HEIGHT - 60))

    # Draw score:
    score_text = score_font.render("TOTAL SCORE: " + str(total_score + round_score), 1, (255, 0, 0))
    screen.blit(score_text, (5, const.SCREEN_HEIGHT - 40))
    # Draw score:
    multiplier_text = score_font.render("MASK MULTIPLIER: " + str(mask_multiplier), 1, (255, 0, 0))
    screen.blit(multiplier_text, (5, const.SCREEN_HEIGHT - 20))

    # Adds a multiplier for wearing mask
    if pygame.sprite.spritecollideany(player, masks):
        mask_multiplier = mask_multiplier + 1



    # Adds TP score if the player got toilet paper
    if pygame.sprite.spritecollideany(player, rolls):
        toilet_paper_score = toilet_paper_score + 100000
        total_score = total_score + toilet_paper_score
    
    # Check if any viruses have collided with the player
    if pygame.sprite.spritecollideany(player, viruses):
        # the player is safe if they're wearing a mask
        if pygame.sprite.spritecollideany(player, masks):
            total_score = total_score + (max(round_score, 1) * max(mask_multiplier, 1))
            mask_multiplier = 0
            round_score = 0
            running = True
        else:
            # If so, then remove the player and stop the loop
            total_score = total_score + round_score
            player.kill()
            running = False

    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 30 frames per second
    clock.tick(60)