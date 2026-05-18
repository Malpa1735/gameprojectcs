import pygame
import random

pygame.init()

# ---------------- WINDOW ----------------
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("QTE Retry System")

clock = pygame.time.Clock()

# ---------------- FONT ----------------
font = pygame.font.SysFont(None, 70)
small_font = pygame.font.SysFont(None, 40)

# ---------------- QTE FUNCTION ----------------
def quick_time_event(screen, clock, keys_needed=4, time_limit=3000):

    possible_keys = [
        pygame.K_w,
        pygame.K_a,
        pygame.K_s,
        pygame.K_d
    ]

    # Generate random sequence
    qte_keys = [random.choice(possible_keys) for _ in range(keys_needed)]

    current_step = 0
    start_time = pygame.time.get_ticks()

    while True:

        current_time = pygame.time.get_ticks()
        elapsed = current_time - start_time

        # ---------- EVENTS ----------
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                expected_key = qte_keys[current_step]

                # Correct key
                if event.key == expected_key:

                    current_step += 1

                    # Finished sequence
                    if current_step >= keys_needed:
                        return True

                # Wrong key
                else:
                    return False

        # ---------- TIMEOUT ----------
        if elapsed >= time_limit:
            return False

        # ---------- DRAW ----------
        screen.fill((25, 25, 25))

        title = font.render(
            "QUICK TIME EVENT",
            True,
            (255, 255, 255)
        )

        screen.blit(title, (180, 100))

        # Draw key sequence
        for i, key in enumerate(qte_keys):

            key_name = pygame.key.name(key).upper()

            # Completed
            if i < current_step:
                color = (0, 255, 0)

            # Current key
            elif i == current_step:
                color = (255, 255, 0)

            # Upcoming
            else:
                color = (255, 255, 255)

            text = font.render(key_name, True, color)

            x = 220 + i * 120
            y = 250

            screen.blit(text, (x, y))

        # ---------- TIMER BAR ----------
        remaining = max(0, time_limit - elapsed)

        bar_width = int((remaining / time_limit) * 500)

        pygame.draw.rect(
            screen,
            (60, 60, 60),
            (200, 400, 500, 35)
        )

        pygame.draw.rect(
            screen,
            (255, 0, 0),
            (200, 400, bar_width, 35)
        )

        pygame.display.flip()
        clock.tick(60)

# ---------------- MAIN LOOP ----------------
run = True

player_value = 100
qte_completed = False

while run:

    screen.fill((40, 40, 40))

    # ---------- EVENTS ----------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:

            # Press SPACE to start QTE
            if event.key == pygame.K_SPACE:

                # Prevent restarting after success
                if qte_completed:
                    print("QTE already completed")
                    continue

                # Repeat until success or value reaches 0
                while player_value > 0:

                    result = quick_time_event(
                        screen,
                        clock,
                        keys_needed=4,
                        time_limit=3000
                    )

                    # SUCCESS
                    if result:

                        print("PLAYER WON QTE")

                        qte_completed = True
                        break

                    # FAILURE
                    else:

                        player_value -= 25

                        print("FAILED")
                        print("VALUE:", player_value)

                # Game over
                if player_value <= 0:
                    print("GAME OVER")

    # ---------- UI TEXT ----------
    if qte_completed:

        message = "QTE COMPLETED"

    elif player_value <= 0:

        message = "GAME OVER"

    else:

        message = "Press SPACE to start QTE"

    info = small_font.render(
        message,
        True,
        (255, 255, 255)
    )

    value_text = small_font.render(
        f"Value: {player_value}",
        True,
        (255, 100, 100)
    )

    screen.blit(info, (260, 260))
    screen.blit(value_text, (360, 320))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()