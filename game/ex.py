import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 200
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Warna
WHITE = (255, 255, 255)

# Fungsi untuk menggambar status plate
def draw_status_plate(surface, player_name, level, health):
    font = pygame.font.Font(None, 24)
    
    # Gambar nama pemain
    name_text = font.render("Name: " + player_name, True, WHITE)
    surface.blit(name_text, (10, 10))
    
    # Gambar level
    level_text = font.render("Level: " + str(level), True, WHITE)
    surface.blit(level_text, (10, 40))
    
    # Gambar health
    health_text = font.render("Health: " + str(health), True, WHITE)
    surface.blit(health_text, (10, 70))

# Fungsi utama
def main():
    # Buat layar
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Status Plate Example")
    
    # Variabel status karakter
    player_name = "Wang Yu"
    level = 'E%$3&4#'
    health = '????'
    
    # Loop utama
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Bersihkan layar
        screen.fill((0, 0, 0))
        
        # Gambar status plate
        draw_status_plate(screen, player_name, level, health)
        
        # Perbarui layar
        pygame.display.flip()

if __name__ == "__main__":
    main()
