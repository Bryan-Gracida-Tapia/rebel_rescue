"""
Nombre del equipo: Átomos
Integrantes: Bryan Gracida Tapia, Addi Toro Chávez
fecha: 10 de junio del 2025
versión: 0.1
- Se muestra una pantalla con un fondo de un solo color y el título de la ventana "Rebel Rescue".
- El único evento que se maneja es cerrar la ventana.
"""

#Se importan los módulos para el videojuego
import pygame

def run_game()->None:
    """
    Función principal del videojuego.
    """
    #Se inicializa el módulo de pygame
    pygame.init()

    #Se inicializa la pantalla
    screen_size=(1280,720)   # Resolución de la pantalla (ancho,alto)
    screen=pygame.display.set_mode(screen_size)

    #Se configura el título del juego
    game_title="Rebel Rescue"
    pygame.display.set_caption(game_title)  #Mostrar título

    #Ciclo principal del videojuego
    game_over=False

    while not game_over:
        #Se verifican los eventos (teclado,ratón) del juego.
        for event in pygame.event.get():
            #Un clic en cerrar el juego
            if event.type == pygame.QUIT:
                game_over=True

        #Se dibujan los elementos gráficos en la pantalla
        background=(50,50,50)  #Fondo de la pantalla en formato RGB
        screen.fill(background)

        #Se actualiza la pantalla
        pygame.display.flip()
    #Se cierran los recursos de pygame
    pygame.quit()

if __name__ == '__main__':
    run_game()