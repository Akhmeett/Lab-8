import pygame
import sys
import math

# Pygame инициализациясы
pygame.init()

# Экран параметрлері
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint App")
clock = pygame.time.Clock()

# Түстер
COLOR_OPTIONS = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255)]
current_color = COLOR_OPTIONS[0]

# Құралдардың кодтары: 0 - карандаш, 1 - тік бұрыш, 2 - шеңбер, 3 - ластик
current_tool = 0
drawing = False
start_pos = None
brush_radius = 5

# Холст параметрлері
canvas = pygame.Surface((800, 600))
canvas.fill((255, 255, 255))  # Ақ түсті холст

# Шрифттер
font = pygame.font.SysFont(None, 24)

# Негізгі цикл
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Түсті өзгерту: Space пернесі арқылы
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            current_color = COLOR_OPTIONS[(COLOR_OPTIONS.index(current_color) + 1) % len(COLOR_OPTIONS)]

        # Құралды өзгерту: 1, 2, 3, 4 пернелері арқылы
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_tool = 0
            elif event.key == pygame.K_2:
                current_tool = 1
            elif event.key == pygame.K_3:
                current_tool = 2
            elif event.key == pygame.K_4:
                current_tool = 3

        # Сурет салуды бастау (кликті басу)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
            start_pos = mouse_pos

        # Сурет салуды аяқтау (фигуралар үшін)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and drawing:
            if current_tool == 1:  # Тік бұрыш
                x = min(start_pos[0], mouse_pos[0])
                y = min(start_pos[1], mouse_pos[1])
                w = abs(mouse_pos[0] - start_pos[0])
                h = abs(mouse_pos[1] - start_pos[1])
                pygame.draw.rect(canvas, current_color, (x, y, w, h), brush_radius)
            elif current_tool == 2:  # Шеңбер
                r = math.sqrt((mouse_pos[0] - start_pos[0]) ** 2 + (mouse_pos[1] - start_pos[1]) ** 2)
                pygame.draw.circle(canvas, current_color, start_pos, int(r), brush_radius)
            drawing = False

    # Карандаш немесе ластикпен сурет салу
    if pygame.mouse.get_pressed()[0] and drawing:
        if current_tool == 0:  # Карандаш
            if start_pos:
                pygame.draw.line(canvas, current_color, start_pos, mouse_pos, brush_radius)
            start_pos = mouse_pos
        elif current_tool == 3:  # Ластик
            pygame.draw.circle(canvas, (255, 255, 255), mouse_pos, brush_radius)

    # Экранға салынған суретті көрсету
    screen.blit(canvas, (0, 0))

    # Құралдар мен түстер туралы ақпаратты көрсету
    tools = ["1-Карандаш", "2-Тік бұрыш", "3-Шеңбер", "4-Ластик"]
    info = f"Құрал: {tools[current_tool]} | Түс: {current_color} (Space - ауыстыру)"
    text = font.render(info, True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Экранды жаңарту
    pygame.display.flip()
    clock.tick(60)

# Ойыннан шығу
pygame.quit()
sys.exit()
