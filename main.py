'''
Main game loop/module
'''

import pygame as pg
import sys
from os import path
import settings
import math
import sprites

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((settings.WIDTH, settings.HEIGHT), vsync=1)
        pg.display.set_caption(settings.TITLE)
        self.clock = pg.time.Clock()
        self.load_data()
        self.running = True
        self.playing = True
        self.mouse_control = True  # toggled with space
        self.all_sprites = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.show_hud = True
        self.new()

    def load_data(self):
        pass

    def new(self):
        self.player = sprites.Player(self, settings.WIDTH/2, settings.HEIGHT/2)
        self.enemy = sprites.Enemy(self, settings.WIDTH/2-settings.TILESIZE, settings.HEIGHT/2-settings.TILESIZE)
        

    def run(self):
        while self.running:
            self.dt = self.clock.tick(settings.FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN 
                and (event.key == pg.K_ESCAPE 
                or event.key == pg.K_q)):
                self.quit()
            if event.type == pg.KEYDOWN:
                match event.key:
                    case pg.K_SPACE:
                        self.mouse_control = not self.mouse_control
                    case pg.K_SLASH:
                        self.show_hud = not self.show_hud
                    

            if event.type == pg.MOUSEBUTTONDOWN:
                print("Mouse clicked at", event.pos)
            if event.type == pg.MOUSEBUTTONUP:
                print("Previous click released at", event.pos)
            

    def update(self):
        self.all_sprites.update(self.dt)

    def draw(self):
        self.screen.fill(settings.BLACK)
        if self.show_hud:
            self.draw_text("FPS", 24, settings.WHITE, settings.WIDTH/2, settings.HEIGHT/4 - settings.TILESIZE)
            self.draw_text(str(math.trunc(1/self.dt)), 24, settings.WHITE, settings.WIDTH/2, settings.HEIGHT/4)
            self.draw_text("Control: " + ("Mouse" if self.mouse_control else "WASD"), 24, settings.WHITE, settings.WIDTH/2, settings.HEIGHT/4 + settings.TILESIZE)
            self.draw_text("Intersecting", 24, settings.WHITE, settings.WIDTH/2, settings.HEIGHT/4 + settings.TILESIZE * 2)
            self.draw_text(str(self.player.check_collision_with_enemies()), 24, settings.WHITE, settings.WIDTH/2, settings.HEIGHT/4 + settings.TILESIZE * 3)
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def quit(self):
        self.playing = False
        self.running = False
        pg.quit()
        sys.exit()



if __name__ == "__main__":
    g = Game()
    g.run()