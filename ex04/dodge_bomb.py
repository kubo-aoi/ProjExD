import pygame as pg
import sys
from random import randint

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900)) # Surface
    screen_rct = screen_sfc.get_rect()            # Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")    # Surface
    bgimg_rct = bgimg_sfc.get_rect()              # Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)
    
    kkimg_sfc = pg.image.load("fig/6.png")
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    kkimg_rct = kkimg_sfc.get_rect()
    kkimg_rct.center = 900, 400

    #爆弾
    bomb = pg.Surface((20,20))                              #爆弾用のsurface
    pg.draw.circle(bomb, (255,0,0),(10,10),10)              #爆弾用surfaceに円を描く。色、中心、半径を指定
    bomb_rct = bomb.get_rect()                             #爆弾用rect
    bomb_rct.centerx = randint(0,screen_rct.width)     #爆弾のx座標をランダムに決定
    bomb_rct.centery = randint(0,screen_rct.height)    #爆弾のy座標をランダムに決定
                               #爆弾用surfaceを画面用surfaceに貼り付ける
    vx, vy = +1, +1

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)

        for event in pg.event.get():              # イベントを繰り返して処理
            if event.type == pg.QUIT:             # ウィンドウの×ボタンをクリックしたら
                return
        
        key_states = pg.key.get_pressed()         # keyの辞書
        if key_states[pg.K_UP] == True:           # ↑が押されたら
            kkimg_rct.centery -= 1                # y座標を-1
        if key_states[pg.K_DOWN] == True:
            kkimg_rct.centery += 1
        if key_states[pg.K_LEFT] == True:
            kkimg_rct.centerx -= 1
        if key_states[pg.K_RIGHT] == True:
            kkimg_rct.centerx += 1
        
        screen_sfc.blit(kkimg_sfc, kkimg_rct)
        
        pg.display.update()
        clock.tick(1000)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()