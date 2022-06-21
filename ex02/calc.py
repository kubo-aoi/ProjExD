import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    #tkm.showinfo("", f"{num}のボタンがクリックされました")
    txt=btn["text"]
    entry.insert(tk.END, txt)

def click(event):
    en = entry.get()
    re = eval(en)
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(re))

def ac_click(event):
    entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("練習問題:calc.py")
    #root.geometry("300x600")

    entry=tk.Entry(root, justify="right", width=10, font=("Times New Roman", 40),
                    bg="white")
    entry.grid(row=0, column=1, columnspan=5)


    rnum = 1
    cnum = 0
    numlist = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, "+", "-", "*", "/"]
    for i, num in enumerate(numlist, 1):
        button = tk.Button(root, text=str(num),
                           font=("Corben", 40), 
                           bg="#58A4B0", fg="white")
        button.grid(row=rnum, column=cnum, sticky=tk.NSEW)
        button.bind("<1>", button_click)
        cnum+=1
        if i%3==0:
            rnum+=1
            cnum=0
        #button.pack()
    
    btn = tk.Button(root, text="=", font=("Time New Roman", 40),
                    bg="white")
    btn.bind("<1>", click)
    btn.grid(row=rnum, column=cnum, sticky=tk.NSEW)

    ac = tk.Button(root, text="AC", font=("Times New Roman", 40),
                    bg="red")
    ac.bind("<1>", ac_click)
    ac.grid(row=rnum, column=cnum+1, sticky=tk.NSEW)


    root.mainloop()