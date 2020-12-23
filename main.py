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

from entities.player import Player
from entities.virus import Virus
from entities.mask import Mask
from entities.toiletPaper import ToiletPaper
from scores import Score

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
GIFIFY = pygame.USEREVENT + 5
pygame.time.set_timer(GIFIFY, 100)

# Instantiate player. 
player = Player()

# Create groups to hold entities
# - individual groups are used for collision detection and position updates
# - all_sprites is used for rendering
viruses = pygame.sprite.Group()
masks = pygame.sprite.Group()
rolls = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Keep track of score
score_font = pygame.font.SysFont("monospace", 16)
mask_count = Score()
total_score = Score()
toilet_paper_score = Score()

# Use this for the proof of concept player gififying
player_image_index = 0

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
        
        # add TP?
        elif event.type == ADDTP:
            new_tp = ToiletPaper()
            rolls.add(new_tp)
            all_sprites.add(new_tp)

        # Iterate score over time
        elif event.type == ADDSCORE:
            total_score.amount += 1

        # gifify the player
        elif event.type == GIFIFY:
            player_image_index += 1
            player.gifify(player_image_index)
    
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
    
    # Draw TP score:
    if toilet_paper_score.amount > 0:
        toilet_paper_upper_text = score_font.render("OMG YOU GOT TOILET PAPER!!!!!", 1, (0, 255, 255))
        screen.blit(toilet_paper_upper_text, (5, 0))

        toilet_paper_lower_text = score_font.render("TOILET PAPER SCORE: " + str(toilet_paper_score.amount), 1, (0, 255, 255))
        screen.blit(toilet_paper_lower_text, (5, const.SCREEN_HEIGHT - 40))

    # Draw total score:
    score_text = score_font.render("TOTAL SCORE: " + str(total_score.amount), 1, (255, 0, 0))
    screen.blit(score_text, (5, const.SCREEN_HEIGHT - 20))

    # Draw mask score:
    mask_text = score_font.render("MASKS: " + str(mask_count.amount), 1, (255, 0, 0))
    screen.blit(mask_text, (5, 20))

    # Adds a SCORE for having a mask
    if pygame.sprite.spritecollideany(player, masks):
        mask_count.update(player, masks, 1)
        # add to the total
        total_score.amount += 100

    # Adds TP score if the player got toilet paper
    if pygame.sprite.spritecollideany(player, rolls):
        toilet_paper_score.update(player, rolls, 1000, mask_count.amount)
        total_score.amount += max(1, mask_count.amount) * 1000
    
    # Check if any viruses have collided with the player
    if pygame.sprite.spritecollideany(player, viruses):
        # the player is safe if they have a mask, but they lose a mask
        if mask_count.amount >= 1:
            mask_count.update(player, viruses, -1)
            # remove the bonus from the mask
            total_score.amount -= 100
        else:
            # If so, then remove the player and stop the loop
            player.kill()
            running = False

    # Update the display
    pygame.display.flip()

    # Ensure program maintains a rate of 60 frames per second
    clock.tick(60)