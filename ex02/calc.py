import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):   #クリックしたときの処理
    btn = event.widget
    x = btn["text"]
    if x == "=":
        eqn = entry.get()
        ans = eval(eqn)
        print(ans)
        entry.delete(0, tk.END)
        entry.insert(tk.END, ans)
    elif x == "d":
        if ans:    #もし表示されているのが計算後だったら・・・という風にしたい
            pass
        else:
            entry.delete(0, 1)
    elif x == "r":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, x)

def button_color(event):
    btn = tk.Button(bg = "gray")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓")
    
    entry = tk.Entry(root, 
                    justify="right",   
                    width=10, 
                    font=("Times New Roman", 40)
                )
    entry.grid(row=0, column=0, columnspan=3)
    
    r, c = 1, 0
    for i, x in enumerate([7, 8, 9, "/", 4, 5, 6, "*", 1, 2, 
                        3, "-", 0, ".", "+", "=", "d", "r"]):
        btn = tk.Button(root, 
                       text=f"{x}", 
                        width=4, 
                        height=2, 
                        font=("Times New Roman", 30), 
                    )
        btn.bind("<1>", button_click)
        btn.bind("<Enter>", button_color)  #マウスオンしたら色が変わる(なぜか変わらない)
        btn.grid(row=r, column=c)
        c += 1
        if (i+1)%4 == 0:
            r += 1
            c = 0

        

    
    root.mainloop()
