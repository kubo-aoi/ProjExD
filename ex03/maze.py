import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    label = tk.Label(root, text="koukaton", font=("Times New Roman", 80))
    label.pack()
    root.mainloop()