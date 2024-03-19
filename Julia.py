import pygame
import sys

# Definir constantes
WIDTH, HEIGHT = 800, 800
PASO = 200
N = 100
DELTA = 4 / PASO
AO = -2
BO = -2

def julia_set(c_r, c_i):
    # Inicializar pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Conjunto de Julia")
    screen.fill((255, 255, 255))

    # Dibujar la red en el plano complejo
    for j in range(PASO):
        for k in range(PASO):
            a = AO + j * DELTA
            b = BO + k * DELTA
            i = 0
            rr = 0

            # Iteración en cada punto
            while i < N and rr < 4:
                an = a * a - b * b + c_r
                b = 2 * a * b + c_i
                a = an
                rr = a * a + b * b
                i += 1
            
            # Dibujar los puntos
            if i < N:
                screen.set_at((int((AO + j * DELTA) * WIDTH / 4 + WIDTH / 2), int((BO + k * DELTA) * HEIGHT / 4 + HEIGHT / 2)), (0, 0, 0))

    # Mantener la ventana abierta
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

# Pedir la constante compleja c
c_r = float(input("Dame la parte real de la constante c: "))
c_i = float(input("Dame la parte imaginaria de la constante c: "))

# Generar el conjunto de Julia con la constante c
julia_set(c_r, c_i)
