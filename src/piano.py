import pygame

pygame.init()
screen = pygame.display.set_mode((980, 320))
pygame.display.set_caption('Piano simulator')
white_keys = []
black_keys = []
gap = 100
WHITE_WIDTH = 136
WHITE_HEIGHT = 320


for key in range(7):
    x = key * (WHITE_WIDTH + 5)
    rect = pygame.Rect(x, 0, WHITE_WIDTH, WHITE_HEIGHT)
    white_keys.append(rect)


black_colour = ('black')
white_colour = ('white')


C_note = pygame.mixer.Sound('notes/C3.wav')
Csh_note = pygame.mixer.Sound('notes/C#3.wav')
D_note = pygame.mixer.Sound('notes/D3.wav')
Dsh_note = pygame.mixer.Sound('notes/D#3.wav')
E_note = pygame.mixer.Sound('notes/E3.wav')
F_note = pygame.mixer.Sound('notes/F3.wav')
Fsh_note = pygame.mixer.Sound('notes/F#3.wav')
G_note = pygame.mixer.Sound('notes/G3.wav')
Gsh_note = pygame.mixer.Sound('notes/G#3.wav')
A_note = pygame.mixer.Sound('notes/A3.wav')
Ash_note = pygame.mixer.Sound('notes/A#3.wav')
B_note = pygame.mixer.Sound('notes/B3.wav')


open = True
while open:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for key, white_key in enumerate(white_keys):
                if white_key.collidepoint(event.pos):
                    C_note.play()
    for white_key in white_keys:
        pygame.draw.rect(screen, 'white', white_key)
    pygame.display.update()
    pygame.time.Clock().tick(60)