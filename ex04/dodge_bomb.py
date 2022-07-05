import pygame as pg
import sys
from random import randint
import time as ti
import tkinter as tk


def main():
    
    time1 = ti.time()

    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1800, 950)) # Surface
    screen_rct = screen_sfc.get_rect()            # Rect

    bgimg_sfc = pg.image.load("fig/yoru.jpg")    # Surface
    bgimg_rct = bgimg_sfc.get_rect()              # Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rct)
    
    kkimg_sfc = pg.image.load("fig/3.png")
    kkimg_sfc = pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    kkimg_rct = kkimg_sfc.get_rect()
    kkimg_rct.center = 900, 400

    #爆弾1
    bmimg_sfc = pg.Surface((40,40))  
    bmimg_sfc.set_colorkey((0, 0, 0))                            #爆弾用のsurface
    pg.draw.circle(bmimg_sfc, (255,255,255),(20,20),20)              #爆弾用surfaceに円を描く。色、中心、半径を指定
    bmimg_rct = bmimg_sfc.get_rect()                             #爆弾用rect
    bmimg_rct.centerx = randint(0,screen_rct.width)     #爆弾のx座標をランダムに決定
    bmimg_rct.centery = randint(0,screen_rct.height)    #爆弾のy座標をランダムに決定
                               #爆弾用surfaceを画面用surfaceに貼り付ける

    #爆弾2
    bmimg_sfc2 = pg.Surface((20,20))  
    bmimg_sfc2.set_colorkey((0, 0, 0))                            #爆弾用のsurface
    pg.draw.circle(bmimg_sfc2, (255,0,0),(10,10),10)              #爆弾用surfaceに円を描く。色、中心、半径を指定
    bmimg_rct2 = bmimg_sfc2.get_rect()                             #爆弾用rect
    bmimg_rct2.centerx = randint(0,screen_rct.width)     #爆弾のx座標をランダムに決定
    bmimg_rct2.centery = randint(0,screen_rct.height)    #爆弾のy座標をランダムに決定

    #爆弾3
    '''
    bomb2=pg.image.load("fig/baku.jpg")
    bomb2 = pg.transform.rotozoom(bomb2,0,2.5)
    bomb2_rect = bomb2.get_rect()                             #爆弾用rect
    bomb2_rect.centerx = randint(0,screen_rct.width)     #爆弾のx座標をランダムに決定
    bomb2_rect.centery = randint(0,screen_rct.height)    #爆弾のy座標をランダムに決定
    vn, vm = +1, +1  
    '''

    vx, vy = +1, +1
    dx, dy = +2, +2

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)

        #pg.draw.ellipse(screen_sfc, (255,0,255), (400,300,200,100))

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
        bmimg_rct.move_ip(vx,vy)                    #1個目の爆弾用のrectを移動する
        screen_sfc.blit(bmimg_sfc, bmimg_rct)                #爆弾の画像を貼り付ける
        yoko, tate = check_bound(screen_rct, bmimg_rct)       #check_bound()関数で画面外にいるかの判定
        vx *= yoko                               #横方向に画面外なら、横方向速度の符号反転
        vy *= tate                               #縦方向に画面外なら、縦方向速度の符号反転

        bmimg_rct2.move_ip(dx,dy)                    #2個目の爆弾
        screen_sfc.blit(bmimg_sfc2, bmimg_rct2)                #爆弾の画像を貼り付ける
        yo, ta = check_bound(screen_rct, bmimg_rct2)       #check_bound()関数で画面外にいるかの判定
        dx *= yo                              #横方向に画面外なら、横方向速度の符号反転
        dy *= ta 

        screen_sfc.blit(bmimg_sfc, bmimg_rct)

        #　爆弾の当たり判定
        if kkimg_rct.colliderect(bmimg_rct) == True: #toriがbombと重なったらTrue
            #pg.time.get_ticks()
            #create_modeless_dialog()
            main()
            return   #終了(mainから抜ける)
        
        if kkimg_rct.colliderect(bmimg_rct2) == True: #toriがbombと重なったらTrue
            return
        
        
        
        pg.display.update()
        clock.tick(1000)

def check_bound(sc_r, obj_r):     #引数は、画面用Rect,{こうかとん,爆弾]Rect
    #画面内なら：+1 / 画面外なら：-1を返す
    x, y = +1, +1
    if obj_r.left < sc_r.left or sc_r.right < obj_r.right:
        x = -1   #画面外に行ったらx=-1
    if obj_r.top < sc_r.top or sc_r.bottom < obj_r.bottom:
        y = -1   #画面外に行ったらy=-1
    return x, y
'''
def create_modeless_dialog(self):
        #モードレスダイアログボックスの作成
        dlg_modeless = tk.Toplevel(self)
        dlg_modeless.title("Modeless Dialog")   # ウィンドウタイトル
        dlg_modeless.geometry("300x200") 
'''
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()