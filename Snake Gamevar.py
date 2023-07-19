import pygame
import random

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // GRID_SIZE, SCREEN_HEIGHT // GRID_SIZE
FPS = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()


# Snake class
class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def move(self, food):
        head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])

        # Wrap around the screen if the snake crosses the boundaries
        head_x, head_y = head
        if head_x < 0:
            head_x = GRID_WIDTH - 1
        elif head_x >= GRID_WIDTH:
            head_x = 0
        if head_y < 0:
            head_y = GRID_HEIGHT - 1
        elif head_y >= GRID_HEIGHT:
            head_y = 0

        head = (head_x, head_y)

        self.body.insert(0, head)

        if head == food:
            return True
        else:
            self.body.pop()
            return False

    def change_direction(self, direction):
        if (direction[0], direction[1]) != (-self.direction[0], -self.direction[1]):
            self.direction = direction

    def check_collision(self):
        return self.body[0] in self.body[1:]

    def draw(self):
        for segment in self.body:
            x, y = segment[0] * GRID_SIZE, segment[1] * GRID_SIZE
            pygame.draw.rect(screen, GREEN, pygame.Rect(x, y, GRID_SIZE, GRID_SIZE))


# Food class
class Food:
    def __init__(self):
        self.position = self.randomize_position()

    def randomize_position(self):
        return random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)

    def draw(self):
        x, y = self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE
        pygame.draw.rect(screen, RED, pygame.Rect(x, y, GRID_SIZE, GRID_SIZE))


# Main function
def main():
    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)

        if snake.move(food.position):
            food.position = food.randomize_position()

        if snake.check_collision():
            pygame.quit()
            quit()

        screen.fill(WHITE)
        snake.draw()
        food.draw()
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
