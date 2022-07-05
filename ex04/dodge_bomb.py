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
    bmimg_sfc = pg.Surface((20,20))  
    bmimg_sfc.set_colorkey((0, 0, 0))                            #爆弾用のsurface
    pg.draw.circle(bmimg_sfc, (255,0,0),(10,10),10)              #爆弾用surfaceに円を描く。色、中心、半径を指定
    bmimg_rct = bmimg_sfc.get_rect()                             #爆弾用rect
    bmimg_rct.centerx = randint(0,screen_rct.width)     #爆弾のx座標をランダムに決定
    bmimg_rct.centery = randint(0,screen_rct.height)    #爆弾のy座標をランダムに決定
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
        if check_bound(screen_rct,kkimg_rct) != (1,1):     #移動後に画面範囲内か
                    if key_states[pg.K_UP] == True:           # ↑が押されたら
                        kkimg_rct.centery += 1                # y座標を-1
                    if key_states[pg.K_DOWN] == True:
                        kkimg_rct.centery -= 1
                    if key_states[pg.K_LEFT] == True:
                        kkimg_rct.centerx += 1
                    if key_states[pg.K_RIGHT] == True:
                        kkimg_rct.centerx -= 1
        
        screen_sfc.blit(kkimg_sfc, kkimg_rct)

         #　爆弾の移動
        bmimg_rct.move_ip(vx,vy)                    #爆弾用のrectを移動する
        screen_sfc.blit(bmimg_sfc, bmimg_rct)                #爆弾の画像を貼り付ける
        yoko, tate = check_bound(screen_rct, bmimg_rct)       #check_bound()関数で画面外にいるかの判定
        vx *= yoko                               #横方向に画面外なら、横方向速度の符号反転
        vy *= tate                               #縦方向に画面外なら、縦方向速度の符号反転

        screen_sfc.blit(bmimg_sfc, bmimg_rct)

        #　爆弾の当たり判定
        if kkimg_rct.colliderect(bmimg_rct) == True: #toriがbombと重なったらTrue
            return #終了(mainから抜ける)
        
        pg.display.update()
        clock.tick(1000)

def check_bound(sc_r, obj_r):     #引数は、画面用Rect,{こうかとん,爆弾]Rect
    #画面内なら：+1 / 画面外なら：-1を返す
    x, y = +1, +1
    if obj_r.left < sc_r.left or sc_r.right < obj_r.right: x = -1   #画面外に行ったらx=-1
    if obj_r.top < sc_r.top or sc_r.bottom < obj_r.bottom: y = -1   #画面外に行ったらy=-1
    return x, y

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()