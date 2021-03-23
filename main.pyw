from helper import *


def main():
    FPS = 60
    run = True
    level = 0
    lives = 5
    wave_length = 5
    enemy_vel = 1
    enemies = []
    lost_count = 0
    laser_vel = 4
    player_vel = 5  # defines player's velocity

    mainfont = pygame.font.SysFont("comicsans", 50)
    Lostfont = pygame.font.SysFont("comicsans", 60)
    Lost = False
    player = Player(300, 630)
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

        if Lost:
            lostLabel = Lostfont.render("You Lost!!", 1, (255, 255, 255))
            WIN.blit(lostLabel, (WIDTH/2 - lostLabel.get_width()/2, 350))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            Lost = True

        if Lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 3
            for i in range(wave_length):
                enemy = Enemy(random.randrange(
                    50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "green", "blue"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.x - player_vel > 0:
            player.x -= player_vel
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.x + player_vel + player.get_width() < WIDTH:
            player.x += player_vel
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.y - player_vel > 0:
            player.y -= player_vel
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.y + player_vel + player.get_height() + 20 < HEIGHT:
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 3*60) == 1:
                enemy.shoot()
            
            if collide(enemy, player):
                player.health -= 20
                enemies.remove(enemy)

            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)

def main_menu():
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        WIN.blit(BG, (0,0))
        title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


main_menu()
