import pygame
pygame.mixer.init()

notes = {
    "C": pygame.mixer.Sound("piano_notes/C3.wav"),
    "D": pygame.mixer.Sound("piano_notes/D3.wav"),
    "E": pygame.mixer.Sound("piano_notes/E3.wav"),
    "F": pygame.mixer.Sound("piano_notes/F3.wav"),
    "G": pygame.mixer.Sound("piano_notes/G3.wav"),
    "A": pygame.mixer.Sound("piano_notes/A3.wav"),
    "B": pygame.mixer.Sound("piano_notes/B3.wav")
}

open = True
while open:
    key = input("Enter a piano key (A, B, C, D, E, F, G) or Q to quit: ").upper()
    if key == 'Q':
        open = False
    if key in notes:
            notes[key].play()