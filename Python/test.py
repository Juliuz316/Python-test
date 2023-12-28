from pygame.math import Vector2

snake_body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]

snake_body[0] = snake_body[0] + (1, 0)
for i, x in enumerate(snake_body):
    print(i, int(x.x), int(x.y))
