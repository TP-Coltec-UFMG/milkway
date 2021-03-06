import pygame
import openal as oal
import openal.al as al
import random
import values


class Asteroides(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        # lista de imagens para asteroide
        images = [
            "assets/images/asteroiderosa_2.png",
            "assets/images/asteroidelaranja1.png",
            "assets/images/asteroideAzul1.png"
        ]
        # variaveis de imagem
        self.image = pygame.image.load(random.choice(images))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

        # seleciona um arquivo aleatorio de audio
        self.source = oal.oalOpen(
            "assets/sounds/b"+str(random.randrange(400, 1100, 100))+".wav")
        self.source.set_looping(True)
        self.source.set_position((x, 0, y))
        self.source.play()

    def destroy(self):
        self.stop_sound(True)

    def update(self):
        """
        Atualiza a posicao do asteroide e a fonte de som dele
        """
        self.rect.y += 2

        # atualizando fonte do som
        self.source.set_position((self.rect.x, 0, self.rect.y/values.f))
        self.source.update()

    def stop_sound(self, deletebuffer=False):
        """
        Encerra o som do asteroide
        """
        self.source.stop()
        # Limpar memória
        b = self.source.buffer
        al.alDeleteSources(1, self.source.id)
        if deletebuffer:
            b.destroy()
