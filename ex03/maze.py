import tkinter as tk
import maze_maker as mm
import tkinter.messagebox as tkm


def key_up(event):
    global key
    key = ""

def key_down(event):
    global key
    key = event.keysym
    #print(f"{key}キーが押されました")

def main_proc():
    global cx, cy, mx, my

    if key == "Up":
        if maze_bg[my-1][mx] == 0:
            my -= 1
    elif key == "Down":
        if maze_bg[my+1][mx] == 0:
            my += 1
    elif key == "Left":
        if maze_bg[my][mx-1] == 0:
            mx -= 1
    elif key == "Right":
        if maze_bg[my][mx+1] == 0:
            mx += 1
    else:
        mx += 0
        my += 0
    
    cx, cy = mx*100+50, my*100+50
    canvas.coords("koukaton", cx, cy)

    if mx == 14:
        if my == 8:
            game_clear()
            entry=tk.Entry(root, justify="right", width=10, font=("Terminal", 40),
                    bg="white") #背景を白に設定
            entry.grid(row=0, column=1, columnspan=5)

#ゴールに着いた時の判定
def game_clear(self):
        #self.playing=False

        self.canvas.create_text(
            750,
            450,
            font=("", 80),
            text="ゲームクリア！"
        )

        self.master.unbind("<KeyPress-Up>")
        self.master.unbind("<KeyPress-Left>")
        self.master.unbind("<KeyPress-Right>")
        self.master.unbind("<KeyPress-Down>")

    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷子のにゃんこ")

    canvas = tk.Canvas(root, width=1500, height=900, bg="blue")
    canvas.pack()
    maze_bg = mm.make_maze(15, 9)
    print(maze_bg)
    mm.show_maze(canvas, maze_bg)

    koukaton = tk.PhotoImage(file="fig/neko.png")
    koukaton = koukaton.zoom(5)
    koukaton = koukaton.subsample(32)
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=koukaton, tag="koukaton")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
#ゴールについたときに文字を表示する
    if mx == 14:
        if my == 8:
            tkm.showwarning(f"GOAL!!!!!Congraturation")
            entry=tk.Entry(root, justify="right", width=10, font=("Terminal", 40),
                    bg="white") #背景を白に設定
    entry.grid(row=0, column=1, columnspan=5)
    main_proc()

    #start = tk.Label(text="START", foreground="white", background="red")
    #start.place(-33, -50)
    
    root.mainloop()