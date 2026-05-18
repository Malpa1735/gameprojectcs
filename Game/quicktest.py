import pygame
import random

pygame.init()

# ---------------- WINDOW ----------------
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reusable QTE Function")

clock = pygame.time.Clock()

# ---------------- FONT ----------------
font = pygame.font.SysFont(None, 70)
small_font = pygame.font.SysFont(None, 40)

# ---------------- QTE FUNCTION ----------------
def quick_time_event(screen, clock, keys_needed=4, time_limit=2000):
    """
    Returns:
        True  = success
        False = failed
    """

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

    run_qte = True

    while run_qte:

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

        title = font.render("QUICK TIME EVENT", True, (255, 255, 255))
        screen.blit(title, (220, 100))

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

        # Timer bar
        remaining = max(0, time_limit - elapsed)
        bar_width = int((remaining / time_limit) * 500)

        pygame.draw.rect(screen, (60, 60, 60), (200, 400, 500, 35))
        pygame.draw.rect(screen, (255, 0, 0), (200, 400, bar_width, 35))

        timer_text = small_font.render("TIME", True, (255, 255, 255))
        screen.blit(timer_text, (200, 360))

        pygame.display.flip()
        clock.tick(60)

# ---------------- MAIN GAME LOOP ----------------
run = True

while run:

    screen.fill((40, 40, 40))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        # Press SPACE to start QTE
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                result = quick_time_event(
                    screen,
                    clock,
                    keys_needed=4,
                    time_limit=3000
                )

                if result:
                    print("PLAYER WON QTE")
                else:
                    print("PLAYER FAILED QTE")

    info = small_font.render(
        "Press SPACE to start QTE",
        True,
        (255, 255, 255)
    )

    screen.blit(info, (250, 280))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()