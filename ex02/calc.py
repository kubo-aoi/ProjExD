import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    button = event.widget
    tkm.showinfo("", f"{num}のボタンがクリックされました")

if __name__ == "__main":
    root = tk.Tk()
    root.title("練習問題:calc.py")
    root.geometry("300x500")

    entry=tk.Entry(root, justify="right", width=10, font=("Times New Roman", 40))
    entry.grid(row=0, column=3, columnspan=3)

    rnum = 1
    cnum = 1
    numlist = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, "+"]
    for i, num in enumerate(numlist, 1):
        button = tk.Button(root, text=str(num),
                           width=4, height=2,
                           font=("Times New Roman", 30))
        button.bind("<1>", button_click)
        button.grid(row=rnum, column=cnum)
        cnum+=1
        if i%3==0:
            rnum+=1
            cnum=0
        #button.pack()


    root.mainloop()