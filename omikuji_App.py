import tkinter as tk
import random
def omikuji():
    kuji = ["大吉","中吉","吉","小吉","凶","大凶"]
    rate = [0,150,400,550,950,1000,1100]
    r = random.randint(1,1100)
    return [kuji[i] for i in range(0,7) if r > rate[i] and r <= rate[i+1]]



def displabel():
    lbl.configure(text = omikuji())

root = tk.Tk()
root.title("おみくじアプリ")
root.geometry("200x100")

lbl = tk.Label(text="LABEL")
btn = tk.Button(text="おみくじ", command = displabel)

btn.pack()
lbl.pack()
tk.mainloop()
