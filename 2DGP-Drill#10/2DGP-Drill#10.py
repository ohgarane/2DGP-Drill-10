from pico2d import *
import random

open_canvas(800, 600)
bird_image = load_image('bird_animation.png')

BIRD_WIDTH, BIRD_HEIGHT = 183, 169
FRAME_COLUMNS, FRAME_ROWS = 5, 3
TOTAL_FRAMES = 14

BIRD_COUNT = 10
BIRD_SCALE = 0.5
FLIGHT_SPEED = 200
FLAP_SPEED = 0.1

class Bird:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = random.randint(100, 500)
        self.speed = FLIGHT_SPEED + random.uniform(-50, 50)
        self.frame = 0
        self.direction = 1

    def update(self, delta_time):
        self.x += self.direction * self.speed * delta_time
        if self.x > 800 or self.x < 0:
            self.direction *= -1
            self.x = max(0, min(self.x, 800))
        self.frame = (self.frame + delta_time / FLAP_SPEED) % TOTAL_FRAMES

    def draw(self):
        frame_x = int(self.frame) % FRAME_COLUMNS * BIRD_WIDTH
        frame_y = int(self.frame) // FRAME_COLUMNS * BIRD_HEIGHT
        if self.direction == 1:
            bird_image.clip_draw(frame_x, frame_y, BIRD_WIDTH, BIRD_HEIGHT, self.x, self.y, BIRD_WIDTH * BIRD_SCALE, BIRD_HEIGHT * BIRD_SCALE)
        else:
            bird_image.clip_composite_draw(frame_x, frame_y, BIRD_WIDTH, BIRD_HEIGHT, 0, 'h', self.x, self.y, BIRD_WIDTH * BIRD_SCALE, BIRD_HEIGHT * BIRD_SCALE)

birds = [Bird() for _ in range(BIRD_COUNT)]

def main():
    running = True
    current_time = get_time()
    while running:
        clear_canvas()
        new_time = get_time()
        delta_time = new_time - current_time
        current_time = new_time

        for bird in birds:
            bird.update(delta_time)
            bird.draw()

        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                running = False

        update_canvas()
        delay(0.01)
main()
close_canvas()
