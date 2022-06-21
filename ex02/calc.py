import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x500")
    root.title("電卓")
    
    btn = tk.Button(root, 
                    text="9", 
                    width=4, 
                    height=2, 
                    font=("Times New Roman", 30), 
                    )
    btn.grid(row=0, column=0)
 
    root.mainloop()
