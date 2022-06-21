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

if __name__ == "__main__":
    root = tk.Tk()
    root.title("練習問題:calc.py")
    #root.geometry("300x600")

    entry=tk.Entry(root, justify="right", width=10, font=("Times New Roman", 30))
    entry.grid(row=0, column=1, columnspan=4)


    rnum = 1
    cnum = 1
    numlist = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, "+"]
    for i, num in enumerate(numlist, 1):
        button = tk.Button(root, text=str(num),
                           font=("Times New Roman", 30))
        button.grid(row=rnum, column=cnum, padx=5, pady=5)
        button.bind("<1>", button_click)
        cnum+=1
        if i%3==0:
            rnum+=1
            cnum=0
        #button.pack()
    
    btn = tk.Button(root, text="=", font=("Times New Roman", 30))
    btn.bind("<1>", click)
    btn.grid(row=rnum, column=cnum, padx=5, pady=5)


    root.mainloop()