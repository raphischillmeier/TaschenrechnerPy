import tkinter as tk

root = tk.Tk()
root.geometry("500x750")
root.maxsize(500, 750)
root.minsize(500, 750)
root.configure(bg="blue")

ausgabe = tk.Label(root, bg="grey", borderwidth=1,  width=72, height=12, text="")
ausgabe.grid(row=1, column=1, columnspan=4)

nine = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="9")
nine.grid(row=2, column=1, columnspan=1)

eight = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="8")
eight.grid(row=2, column=2, columnspan=1)

seven = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="7")
seven.grid(row=2, column=3, columnspan=1)

plus = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="+")
plus.grid(row=2, column=4, columnspan=1)

six = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="6")
six.grid(row=3, column=1, columnspan=1)

five = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="5")
five.grid(row=3, column=2, columnspan=1)

four = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="4")
four.grid(row=3, column=3, columnspan=1)

minus = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="-")
minus.grid(row=3, column=4, columnspan=1)

three = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="3")
three.grid(row=4, column=1, columnspan=1)

two = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="2")
two.grid(row=4, column=2, columnspan=1)

one = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="1")
one.grid(row=4, column=3, columnspan=1)

addit = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="*")
addit.grid(row=4, column=4, columnspan=1)

noo = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="<-")
noo.grid(row=5, column=1, columnspan=1)

zero = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="0")
zero.grid(row=5, column=2, columnspan=1)

komma = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text=",")
komma.grid(row=5, column=3, columnspan=1)

div = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="/")
div.grid(row=5, column=4, columnspan=1)

enter = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="Enter")
enter.grid(row=6, column=1, columnspan=3)

delete = tk.Button(root, bg="white", borderwidth=1, width=16, height=8, text="Del")
delete.grid(row=6, column=4, columnspan=1)

root.mainloop()