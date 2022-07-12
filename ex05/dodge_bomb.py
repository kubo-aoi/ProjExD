import pygame as pg
import sys
import random
import os

#img_bg = pg.image.load("fig/bgimage.png")
#img_bg = pg.transform.rotozoom(img_player,0,0.5)
#img_player = pg.image.load("fig/player.jpg")
#img_player = pg.transform.rotozoom(img_player,0,0.5)
#img_weapon = pg.image.load("fig/bullet.jpg")
bg_y = 0
#px = 320 #プレイヤーのX座標
#py = 240 #プレイヤーのY座標
#bx = 0 #弾のX座標
#by = 0 #弾のY座標
space = 0
BULLET_MAX = 100 #弾の最大値
bull_n = 0
bull_x =[0]*BULLET_MAX
bull_y =[0]*BULLET_MAX
bull_f =[False]*BULLET_MAX


# def load_image(file):
#     """loads an image, prepares it for play"""
#     file = os.path.join(main_dir, "data", file)
#     try:
#         surface = pg.image.load(file)
#     except pg.error:
#         raise SystemExit('Could not load image "%s" %s' % (file, pg.get_error()))
#     return surface.convert()

class Screen:
    def __init__(self, title, widhei, imgfile):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(widhei)        # Surface
        self.rct = self.sfc.get_rect()                # Rect
        self.bgi_sfc = pg.image.load(imgfile)         # Surface
        self.bgi_sfc = pg.transform.rotozoom(self.bgi_sfc, 0, 2)
        self.bgi_rct = self.bgi_sfc.get_rect()                # Rect
        self.bgi_rct.center = (900, bg_y+200)
    
    def update(self):
        global bg_y
        self.bgi_rct.center = (900, bg_y+200)
        if check_bound(self.bgi_rct, self.rct) != (1, 1):# 領域外だったら
            bg_y = 0
            self.bgi_rct.center = (900, 200) 

            

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    def __init__(self, imgfile, size, zahyou):
        self.sfc = pg.image.load(imgfile)             # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()                # Rect
        self.rct.center = zahyou
    
    def blit(self, screen: Screen):
        screen.sfc.blit(self.sfc, self.rct)           #screen_sfc.blit(kkimg_sfc, kkimg_rct)

    def update(self, screen:Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]:
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]:
            self.rct.centery += 1
        if key_states[pg.K_LEFT]:
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            self.rct.centerx += 1
        # 練習7
        if check_bound(self.rct, screen.rct) != (1, 1): # 領域外だったら
                if key_states[pg.K_UP]:
                    self.rct.centery += 1
                if key_states[pg.K_DOWN]:
                    self.rct.centery -= 1
                if key_states[pg.K_LEFT]:
                    self.rct.centerx += 1
                if key_states[pg.K_RIGHT]:
                    self.rct.centerx -= 1
        self.blit(screen)


class Bomb:
    def __init__(self, color, size, vxy, screen:Screen):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, screen.rct.width)
        self.rct.centery = random.randint(0, screen.rct.height)
        self.vx, self.vy = vxy
    
    def blit(self, screen: Screen):
        screen.sfc.blit(self.sfc, self.rct)

    def update(self, screen:Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, screen.rct)
        self.vx *= yoko
        self.vy *= tate
        # 練習5
        #screen.sfc.blit(self.sfc, self.rct)
        self.blit(screen)

'''
class Background:
    def __init__(self, imgfile, size):
        self.image = pg.image.load(imgfile).convert_alpha()    #画像をtransformでサイズ調整
        self.image = pg.transform.scale(self.image, size)  #sizeは(width, height)
        #画面のスクロール設定
        self.scroll = 0
        self.scroll_speed = 4
        self.x = 0
        self.y = 0
        #0と画面横サイズの二つをリストに入れておく
        self.imagesize = [0,950]
    
    def blit(self, screen:Screen):
        self.image.blit(self.image, self.scroll + self.imagesize[0], self.y)
        self.image.blit(self.image, self.scroll + self.imagesize[1], self.y)

    #描画メソッド
    def draw_BG(self,screen): 
        #for文で２つの位置に１枚づつバックグラウンドを描画する（描画するx位置は上で指定したimagesizeリスト）
        for i in range(2):      
            screen.blit(self.image,(self.scroll + self.imagesize[i], self.y))
        self.scroll -= self.scroll_speed
        #画像が端まで来たら初期位置に戻す
        if abs(self.scroll) > 950:
            self.scroll = 0

    #def update(self, screen:Screen):
        #self.BG.draw_BG(self.screen)
        #self.blit(screen)
'''

# def set_bullet():#弾のスタンバイ
#     global bull_n
#     bull_f[bull_n] = True
#     bull_x[bull_n] = px-16
#     bull_y[bull_n] = py-32
#     bull_n = (bull_n+1)%BULLET_MAX

# def move_bullet(screen):#弾を飛ばす
#     for i in range(BULLET_MAX):
#         if bull_f[i] == True:
#             bull_y[i] = bull_y[i] - 32
#             screen.blit(img_weapon,[bull_x[i],bull_y[i]])
#             if bull_y[i] < 0:
#                 bull_f[i] = False

# def move_player(screen,key):
#     global px,py,space
#     if key[pg.K_UP] == 1:
#         py = py - 10
#         if py < 20:
#             py = 20
#     if key[pg.K_DOWN] == 1:
#         py = py + 10
#         if py > 460:
#             py = 460
#     if key[pg.K_LEFT] == 1:
#         px = px - 10
#         if px < 20:
#             px = 20
#     if key[pg.K_RIGHT] == 1:
#         px = px + 10
#         if px > 620:
#             px = 620
#     space = (space+1)*key[pg.K_SPACE]
    # if space%5 == 1: #5フレーム毎に弾を飛ばす
    #     set_bullet()

    #screen.blit(img_player,[px-16,py-16])

class Shot(pg.sprite.Sprite):
    """a bullet the Player sprite fires."""

    speed = -11
    images = []

    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        """called every time around the game loop.

        Every tick we move the shot upwards.
        """
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
            self.kill()


def main():
    clock = pg.time.Clock()
    scr = Screen("逃げろ！こうかとん", (1800, 950), "fig/bgimage.png")
    kkt = Bird("fig/player.jpg", 0.2, (900, 400))
    bkd = Bomb((255, 0, 0), 10, (+5, +5), scr)  #赤、速度１
    #bg = Background("fig/yoru.jpg", (1800, 950))
    global bg_y
    #pg.init()
    #pg.display.set_caption("シューティングゲーム")
    #screen = pg.display.set_mode((640,480))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        bg_y += 5
        scr.update()
        
        scr.blit()
        #key = pg.key.get_pressed()
        #move_player(scr,key)
        #move_bullet(screen)
        #pg.display.update()
        #clock.tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
    
        kkt.update(scr)
        bkd.update(scr)
        #bg.update(scr)
        #bg.draw_BG(scr)
        #Shot.images = [load_image("shot.gif")]


        # 練習8
        #if kkimg_rct.colliderect(bmimg_rct): return 
        if kkt.rct.colliderect(bkd.rct):
            return

        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()