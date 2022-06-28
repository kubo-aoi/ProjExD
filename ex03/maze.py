import tkinter as tk
import maze_maker as mm

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
        my -=1
    elif key == "Down":
        my += 1
    elif key == "Left":
        mx -= 1
    elif key == "Right":
        mx += 1
    else:
        mx += 0
    
        my += 0
    cx, cy = mx*100+50, my*100+50
    canvas.coords("koukaton", cx, cy)
    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()
    maze_bg = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_bg)

    koukaton = tk.PhotoImage(file="fig/0.png")
    mx, my = 1, 1
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=koukaton, tag="koukaton")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()
    
    root.mainloop()