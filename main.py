import tkinter as tk

calculation = ""
def addCalculation(zahl):
    global calculation
    zahl = str(zahl)
    calculation = calculation + zahl
    ausgabe.config(text=calculation)

def evalCalculation():
    global calculation
    calculation = eval(calculation)
    ausgabe.config(text=calculation)

def delete():
    global calculation
    calculation = ""
    ausgabe.config(text="")

def deleteLast():
    global calculation
    calculation = calculation[:-1]
    ausgabe.config(text=calculation)



root = tk.Tk()
root.geometry("500x750")
root.maxsize(500, 750)
root.minsize(500, 750)
root.configure(bg="blue")

ausgabe = tk.Label(root, bg="grey", borderwidth=1,  width=72, height=12, text="")
ausgabe.grid(row=1, column=1, columnspan=4, sticky="nsew")
ausgabe.config(fg="black")

nine = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="9", command=lambda: addCalculation("9"))
nine.grid(row=2, column=1, columnspan=1, sticky="nsew")

eight = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="8", command=lambda: addCalculation("8"))
eight.grid(row=2, column=2, columnspan=1, sticky="nsew")

seven = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="7", command=lambda: addCalculation("7"))
seven.grid(row=2, column=3, columnspan=1, sticky="nsew")

plus = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="+", command=lambda: addCalculation("+"))
plus.grid(row=2, column=4, columnspan=1, sticky="nsew")

six = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="6", command=lambda: addCalculation("6"))
six.grid(row=3, column=1, columnspan=1, sticky="nsew")

five = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="5", command=lambda: addCalculation("5"))
five.grid(row=3, column=2, columnspan=1, sticky="nsew")

four = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="4", command=lambda: addCalculation("4"))
four.grid(row=3, column=3, columnspan=1, sticky="nsew")

minus = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="-", command=lambda: addCalculation("-"))
minus.grid(row=3, column=4, columnspan=1, sticky="nsew")

three = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="3", command=lambda: addCalculation("3"))
three.grid(row=4, column=1, columnspan=1, sticky="nsew")

two = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="2", command=lambda: addCalculation("2"))
two.grid(row=4, column=2, columnspan=1, sticky="nsew")

one = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="1", command=lambda: addCalculation("1"))
one.grid(row=4, column=3, columnspan=1, sticky="nsew")

addit = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="*", command=lambda: addCalculation("*"))
addit.grid(row=4, column=4, columnspan=1, sticky="nsew")

noo = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="<-", command=deleteLast)
noo.grid(row=5, column=1, columnspan=1, sticky="nsew")

zero = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="0", command=lambda: addCalculation("0"))
zero.grid(row=5, column=2, columnspan=1, sticky="nsew")

komma = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text=",", command=lambda: addCalculation("."))
komma.grid(row=5, column=3, columnspan=1, sticky="nsew")

div = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="/", command=lambda: addCalculation("/"))
div.grid(row=5, column=4, columnspan=1, sticky="nsew")

enter = tk.Button(root, bg="white", borderwidth=1, width=16, height=7, text="Enter", command=evalCalculation)
enter.grid(row=6, column=1, columnspan=3, sticky="nsew")

delete = tk.Button(root, bg="white", borderwidth=1, width=16, height=8, text="Del", command=delete)
delete.grid(row=6, column=4, columnspan=1, sticky="nsew")

root.mainloop()