from setup import *
from Ship import *
from Enemy import *
from Particle import *
# every 500 iterations, enemy spawns.
enemySpawnTimer = 0

integrity = 100
kills = 0

hudFont = pygame.font.Font("Minecraftia.ttf", 16)
endFont = pygame.font.Font("Minecraftia.ttf", 32)
gameEndFont = hudFont.render("GAME OVER", False, pygame.color.Color("white"))

gameEnd = False



def showhud():
    hudFontRender = hudFont.render("Integrity: " + str(integrity), False, pygame.color.Color("orange"))
    killsFontRender = hudFont.render("Terminations: " + str(kills), False, pygame.color.Color("green"))

    DISPLAY.blit(hudFontRender, (0,0))
    DISPLAY.blit(killsFontRender, (0, 20))

partspawnrate = 0

spawnrate = 1500.0
gametimerthing = 0
def restart():
    print('restarted')
    gameEnd = False
    gametimerthing = 0
    kills = 0
    integrity = 100
    enemies = []
    bullets = []
gameovercolor = pygame.color.Color("white")
while True:
    DISPLAY.fill(pygame.color.Color(30, 40, 34))
    if gameEnd:
        enemies = []
        gametimerthing += 1
        if gametimerthing == 50:
            gameovercolor = pygame.color.Color("red")
        if gametimerthing == 100:
            gameovercolor = pygame.color.Color("white")
            gametimerthing = 0
        endFontRender = endFont.render("GAME OVER", False, gameovercolor)
        DISPLAY.blit(endFontRender, (
        WIDTH / 2 - (endFontRender.get_rect().size[0] / 2), HEIGHT / 2 - (endFontRender.get_rect().size[1] / 2)))
    else:
        mousePos = pygame.mouse.get_pos()
        ship.pos["x"] = mousePos[0]
        showhud()
    partspawnrate += 1
    if partspawnrate == 20:
        particles.append(Particle())
        partspawnrate = 0

    if integrity < 0:
        gameEnd = True
        integrity = 0

    enemySpawnTimer += 1
    if enemySpawnTimer == spawnrate:
        enemies.append(Enemy(random.randint(0, WIDTH - 50), 0))
        enemySpawnTimer = 0
    ship.update()
    keys = pygame.key.get_pressed()

    # deprecated
    # if keys[K_UP]:
    #     ship.pos["y"] -= 0.5
    # if keys[K_DOWN]:
    #     ship.pos["y"] += 0.5
    # if keys[K_LEFT]:
    #     ship.pos["x"] -= 0.5
    # if keys[K_RIGHT]:
    #     ship.pos["x"] += 0.5
    if keys[K_SPACE]:
        ship.delayer += 1
        if ship.delayer == 200:
            ship.delayer = 0
            bullets.append(Bullet(ship.pos["x"], ship.pos["y"]))

    for i in enemies:
        if i.update():
            integrity -= 5

    for i in bullets:
        if i.update():
            kills += 1

    for i in particles:
        if i.update():
            i.destroy()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_r:
                restart()


    pygame.display.update()