from ships import *


def main():
    FPS = 60
    run = True
    level = 0
    lives = 5
    wave_length = 5
    enemy_vel = 1
    enemies = []
    player_vel = 5  # defines player's velocity

    mainfont = pygame.font.SysFont("Anonymous Pro", 50)
    player = Player(300, 650)
    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0, 0))
        lives_label = mainfont.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = mainfont.render(f"Level: {level}", 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width(), 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)

        if len(enemies) == 0:
            level += 1
            wave_length += 3
            for i in range(wave_length):
                enemy = Enemy(random.randrange(
                    50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "green", "blue"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.x - player_vel > 0:
            player.x -= player_vel
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.x + player_vel + player.get_width() < WIDTH:
            player.x += player_vel
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.y - player_vel > 0:
            player.y -= player_vel
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.y + player_vel + player.get_height() < HEIGHT:
            player.y += player_vel
        
        for enemy in enemies:
            enemy.move(enemy_vel)

        redraw_window()

main()
