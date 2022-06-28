import tkinter as tk

def key_up():
    global key
    key = ""

def key_down(event):
    global key
    key = event.keysym
    print(f"{key}キーが押されました")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()
    koukaton = tk.PhotoImage(file="fig/0.png")
    cx, cy = 300, 400
    canvas.create_image(cx, cy, image=koukaton, tag="koukaton")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up())
    root.mainloop()