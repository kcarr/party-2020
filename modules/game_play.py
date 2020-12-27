# Import the pygame module
import pygame

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from enum import Enum
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from modules.entities.player import Player
from modules.entities.virus import Virus
from modules.entities.mask import Mask
from modules.entities.toiletPaper import ToiletPaper
from modules.scores import Score
from constants import (
    VIRUS_TIMER,
    MASK_TIMER,
    SCORE_TIMER,
    TP_TIMER,
    GIFIFY_TIMER,
    TIME_SCORE,
    SCREEN_HEIGHT,
    MASK_SCORE,
    TP_SCORE,
)

class GameMode(Enum):
    #### GAME MODES ####
    QUIT = 0
    TITLE_SCREEN = 1
    GAME_SCREEN = 2

class GamePlay():
    def __init__(self, screen):
        # Fill the screen with black
        screen.fill((0, 0, 0))

    def playing(self, screen):
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
        playGame = True

        # Setup the clock for a decent framerate
        clock = pygame.time.Clock()

        # Create a custom events for adding new entities
        ADDVIRUS = pygame.USEREVENT + 1
        pygame.time.set_timer(ADDVIRUS, VIRUS_TIMER)
        ADDMASK = pygame.USEREVENT + 2
        pygame.time.set_timer(ADDMASK, MASK_TIMER)
        ADDSCORE = pygame.USEREVENT + 3
        pygame.time.set_timer(ADDSCORE, SCORE_TIMER)
        ADDTP = pygame.USEREVENT + 4
        pygame.time.set_timer(ADDTP, TP_TIMER)
        GIFIFY = pygame.USEREVENT + 5
        pygame.time.set_timer(GIFIFY, GIFIFY_TIMER)

        # Main loop
        while playGame:
            # Look at every event in the queue
            for event in pygame.event.get():
                # Did the user hit a key?
                if event.type == KEYDOWN:
                    # Was it the Escape key? If so, stop the loop.
                    if event.key == K_ESCAPE:
                        playGame = False
                    
                # Did the user click the window close button? If so, stop the loop
                elif event.type == QUIT:
                    playGame = False
            
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
                    total_score.update(TIME_SCORE)

                # gifify the player
                elif event.type == GIFIFY:
                    player_image_index += 1
                    player.gifify(player_image_index)
            
            # Fill the screen with black
            screen.fill((0, 0, 0))
            
            # Get the set of keys pressed and check for user input
            pressed_keys = pygame.key.get_pressed()

            # Update positions
            masks.update()
            player.update(pressed_keys)
            viruses.update()
            rolls.update()

            # Draw all sprites
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            
            # Draw TP score:
            if toilet_paper_score.amount > 0:
                toilet_paper_upper_text = score_font.render("OMG YOU GOT TOILET PAPER!!!!!", 1, (0, 255, 255))
                screen.blit(toilet_paper_upper_text, (5, 0))

                toilet_paper_lower_text = score_font.render("TOILET PAPER SCORE: " + str(toilet_paper_score.amount), 1, (0, 255, 255))
                screen.blit(toilet_paper_lower_text, (5, SCREEN_HEIGHT - 40))

            # Draw total score:
            score_text = score_font.render("TOTAL SCORE: " + str(total_score.amount), 1, (255, 0, 0))
            screen.blit(score_text, (5, SCREEN_HEIGHT - 20))

            # Draw mask score:
            mask_text = score_font.render("MASKS: " + str(mask_count.amount), 1, (255, 0, 0))
            screen.blit(mask_text, (5, 20))

            # Adds a SCORE for having a mask
            if pygame.sprite.spritecollideany(player, masks):
                mask_count.update_collision(player, masks, 1)
                # add to the total
                total_score.update(MASK_SCORE)

            # Adds TP score if the player got toilet paper
            if pygame.sprite.spritecollideany(player, rolls):
                toilet_paper_score.update_collision(player, rolls, TP_SCORE, mask_count.amount)
                total_score.update(TP_SCORE, mask_count.amount)
            
            # Check if any viruses have collided with the player
            if pygame.sprite.spritecollideany(player, viruses):
                # the player is safe if they have a mask, but they lose a mask
                if mask_count.amount >= 1:
                    mask_count.update_collision(player, viruses, -1)
                    # remove the mask bonus from the total
                    total_score.update(-MASK_SCORE)
                else:
                    # If so, then remove the player and stop the loop
                    player.kill()
                    playGame = False

            # Update the display
            pygame.display.flip()

            # Ensure program maintains a rate of 60 frames per second
            clock.tick(60)

        return GameMode.TITLE_SCREEN