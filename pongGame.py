# Pong Game with pygame

from pygame import *
from random import choice
import sys

class PongGame:
    # Constant game variables
    WIDTH, HEIGHT = 800, 500
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    PADDLE_WIDTH = 15
    PADDLE_HEIGTH = 100
    PADDLE_SPEED = 10
    BALL_RADIUS = 15
    BALL_SPEED_X = 3
    BALL_SPEED_Y = 3

    def __init__(self):
        # Game settings
        font.init()
        mixer.init()

        self.screen = display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = time.Clock()
        display.set_caption("pypong 5.0")

        bounce_sound = mixer.Sound("rubberballbouncing-251948.mp3")
        bounce_sound.set_volume(0.5)
        bounce_sound.play()

        #Game variables
        self.player1 = [50, (self.HEIGHT - self.PADDLE_HEIGTH)/2]
        self.player2 = [self.WIDTH - 50 - self.PADDLE_WIDTH, (self.HEIGHT - self.PADDLE_HEIGTH)/2]
        self.ball_position = [self.WIDTH//2, self.HEIGHT//2]
        self.ball_speed = [self.BALL_SPEED_X, self.BALL_SPEED_Y]
        self.p1_score = 0
        self.p2_score = 0
        self.font = font.Font(None, 45)

    #Make the paddles
    def paddle(self, pos):
        draw.rect(self.screen, self.WHITE, (pos[0], pos[1], self.PADDLE_WIDTH, self.PADDLE_HEIGTH))

    # Make a ball
    def ball(self, pos):
        draw.circle(self.screen, self.WHITE, pos, self.BALL_RADIUS)

    # Check if ball hits paddle:
    def hit_paddle(self, ball_position, paddle_pos) -> bool:
        return (paddle_pos[0] < ball_position[0] < paddle_pos[0] + self.PADDLE_WIDTH) and (paddle_pos[1] < ball_position[1] < paddle_pos[1] + self.PADDLE_HEIGTH)

    # Move the ball
    def update_ball(self):
        self.ball_position[0] += self.ball_speed[0]
        self.ball_position[1] += self.ball_speed[1]

        if self.ball_position[1] - self.BALL_RADIUS <= 0 or self.ball_position[1] +self.BALL_RADIUS >= self.HEIGHT - self.BALL_RADIUS:
            self.ball_speed[1] = -self.ball_speed[1]

        if self.hit_paddle(self.ball_position, self.player1) or self.hit_paddle(self.ball_position, self.player2):
             self.ball_speed[0] = -self.ball_speed[0]

        if self.ball_position[0] <= 0:
            self.p2_score += 1
            self.reset()

        if self.ball_position[0] >= self.WIDTH:
            self.p1_score += 1
            self.reset()

    # reset the game
    def reset(self):
        self.ball_position = [self.WIDTH//2, self.HEIGHT//2]
        random_direction = choice([-1, 1])
        self.ball_speed = [self.BALL_SPEED_X * random_direction, self.BALL_SPEED_Y]

    #  # Run the game
    def run_game(self):
        run = True
        while run:  # inner loop → one match
            for e in event.get():
                if e.type == QUIT:
                    run = False
                    sys.exit()

            keys = key.get_pressed()
            if keys[K_w] and self.player1[1] >0:
                self.player1[1] -= self.PADDLE_SPEED
            elif keys[K_s] and self.player1[1] < self.HEIGHT - self.PADDLE_HEIGTH:
                self.player1[1] += self.PADDLE_SPEED

            if keys[K_UP] and self.player2[1] >0:
                self.player2[1] -= self.PADDLE_SPEED
            elif keys[K_DOWN] and self.player2[1] < self.HEIGHT - self.PADDLE_HEIGTH:
                self.player2[1] += self.PADDLE_SPEED

            self.update_ball()
            self.screen.fill(self.BLACK)
            self.paddle(self.player1)
            self.paddle(self.player2)
            self.ball(self.ball_position)

            p1_text = self.font.render(str(self.p1_score), True, self.WHITE)
            p2_text = self.font.render(str(self.p2_score), True, self.WHITE)

            self.screen.blit(p1_text, (self.WIDTH/4, 20))
            self.screen.blit(p2_text, (self.WIDTH * 3 /4, 20))

            # winning condition
            if self.p1_score >= 5 or self.p2_score >= 5:
                run = False

            display.update()
            self.clock.tick(40)

if __name__ == "__main__":
    print("starting game...")
    game = PongGame()
    game.run_game()
   




   
   













