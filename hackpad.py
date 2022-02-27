from tkinter import *
from tkinter import ttk
import json
from functools import partial


button_columns = 3

def fill_output(params, ctext):

    output.delete(0, END)
    output.insert(0, ctext)
    return

with open("config.json", "r") as f:
    configs = json.loads(f.read())

print(configs)

root = Tk()
root.title("Hackpad")
root.iconbitmap("images/winged-arrow_38729.ico")

output_label = Label(root, text="Copy String")
output = Entry(root, width=50)

buttons = []
for key in configs["sections"][0]["keys"]:
    # fill_out2 = fill_output(key["parms"], key["ctext"])
    fill_output2 = partial(fill_output, key["parms"], key["ctext"])
    buttons.append(Button(root, text=key["qname"], width=15, height=5, command=fill_output2))

b_row = 0
for i, button in enumerate(buttons):

    if i != 0 and i % button_columns == 0:
        b_row += 1

    button.grid(row=b_row, column=i % button_columns)



output_label.grid(row=b_row+1, column=0, columnspan=button_columns)
output.grid(row=b_row+2, column=0, columnspan=button_columns)

root.mainloop()