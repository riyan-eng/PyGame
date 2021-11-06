# mengimport modul pygame
import pygame

# bikin variabel 
tinggi = 400
lebar = 600

# perintah untuk menginisialisasi pygame
pygame.init()

# vaiabel ini akan digunakan untuk membuat jendela
layar = pygame.display.set_mode((lebar, tinggi))

selesai = False

while not selesai:
    # ini akan mengosongkan antrian acara/task yang berjan
    # jika kita tidak memanggil event ini, jendela akan
    # menumpuk terus
    for event in pygame.event.get():
        # ini adalah tipe even yang digunakan untuk
        # menutup jendela
        if event.type == pygame.QUIT:
            selesai = True

    # perintah ini diperlukan untuk menampilkan semua pembaruan 
    # yang terjadi
    pygame.display.flip()