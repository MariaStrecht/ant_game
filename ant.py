import pygame

WIDTH, HEIGHT = 80, 40
SCALE = 17

class Ant:    
    def __init__(self):
        self.body = [(40, 20)]
        
        
    def draw(self,display):
        for x, y in self.body:
            pygame.draw.rect(display, "black", (SCALE * x, SCALE * y, SCALE, SCALE)) 

        
    def move(self,direction):
        tmp_1 = self.body[0][0] + direction[0]
        tmp_2 = self.body[0][1] + direction[1]
        
        if tmp_1 > (WIDTH-1) or tmp_2 > (HEIGHT-1):
            return
        
        # move snake
        # colocar a cabeça da snake na direção
        self.body[0:0] = [
            (tmp_1, tmp_2)
        ]


        # apagar a cauda da snake (manter o tamanho)
        while len(self.body) > 1:
            self.body.pop()
