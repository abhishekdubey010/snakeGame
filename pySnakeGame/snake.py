import pygame
import random
pygame.init()

#Creating window
screen_width = 900
screen_height = 600
game_window = pygame.display.set_mode((screen_width, screen_height))

#Game title
pygame.display.set_caption('Snake Game')
pygame.display.update()

#colour
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)


clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text,color,x,y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x,y])

def plot_snake(game_window, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window, black, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        game_window.fill((233,210,229))
        text_screen("Welcome to Snakes", black, 260, 250)
        text_screen("Press Space Bar To Play", black, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(60)


# Game Loop
def gameloop():
    # some variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 50
    snake_size = 20
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(0, screen_width)
    food_y = random.randint(0, screen_height)
    snk_list = []
    snk_length = 1
    init_velocity = 7
    score = 0
    fps = 30
    with open('highscore.txt', 'r') as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            with open('highscore.txt', 'w') as f:
                f.write(str(highscore))

            game_window.fill(white)
            text_screen('Game Over! Please Enter to continue.', red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = - init_velocity
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = init_velocity

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<15 and abs(snake_y - food_y)<15:   ###abs give absolute value
                score +=10
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snk_length += 5
                if score>int(highscore):
                    highscore = score

            game_window.fill(white)
            text_screen('Score: ' +str(score)+ '    Highcore: ' +str(highscore), red, 5,5)
            pygame.draw.rect(game_window, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True

            plot_snake(game_window, black, snk_list, snake_size )
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
welcome()