import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    x = btn["text"]
    if x == "=":
        eqn = entry.get()
        ans = eval(eqn)
        print(ans)
        entry.delete(0, tk.END)
        entry.insert(tk.END, ans)
    else:
        entry.insert(tk.END, x)



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
    for i, x in enumerate([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, "+", "="]):
        btn = tk.Button(root, 
                       text=f"{x}", 
                        width=4, 
                        height=2, 
                        font=("Times New Roman", 30), 
                    )
        btn.bind("<1>", button_click)
        btn.grid(row=r, column=c)
        c += 1
        if (i+1)%3 == 0:
            r += 1
            c = 0

        

    
    root.mainloop()
