from tkinter import *
from tkinter import ttk
import json
from functools import partial


button_columns = 4

def fill_output(parms, ctext):

    output.delete(0, END)
    print("in fill_output")
    for parm in parms:
        val = parm_dict[parm].get()
        print(val)
        if val:
            ctext = ctext.replace("{"+parm+"}", val)

    output.insert(0, ctext)
    return

def main():
    with open("config.json", "r") as f:
        configs = json.loads(f.read())

    root = Tk()
    root.title("Hackpad")
    # root.iconbitmap("images/winged-arrow_38729.ico")

    parms_frame = LabelFrame(root, text="Parameters", padx=5, pady=5)
    parms_frame.grid(row=0, column=0, padx=10, pady=10)

    button_notebook = ttk.Notebook(root)
    button_notebook.grid(row=1, column=0)

    output_frame = LabelFrame(root, text="Output", padx=5, pady=5)
    output_frame.grid(row=2, column=0, padx=10, pady=10)

    sections = []
    parms = []
    for j, section in enumerate(configs["sections"]):
        sections.append(LabelFrame(button_notebook, text=section["title"]))
        sections[j].pack(fill="both", expand=1)
        buttons = []
        for key in section["keys"]:
            fill_output2 = partial(fill_output, key["parms"], key["ctext"])
            buttons.append(Button(sections[j], text=key["qname"], width=15, height=5, command=fill_output2))
            parms += key["parms"]

        b_row = 0
        for i, button in enumerate(buttons):

            if i != 0 and i % button_columns == 0:
                b_row += 1

            button.grid(row=b_row, column=i % button_columns)

        button_notebook.add(sections[j],text=section["title"])

    parms = list(set(parms))
    print(parms)

    parm_frames = []
    global parm_dict
    parm_dict = {}
    for i, parm in enumerate(parms):
        parm_frames.append(Frame(parms_frame, borderwidth=0, highlightthickness=0))
        Label(parm_frames[-1], text=parm).grid(row=0, column=0)
        parm_dict[parm] = Entry(parm_frames[-1], width=30)
        parm_dict[parm].grid(row=1, column=0)

    f_row=0
    for i, frame in enumerate(parm_frames):
        if i != 0 and i % 2 == 0:
            f_row += 1
        frame.grid(row=f_row, column= i % 2)





    output_label = Label(output_frame, text="Copy String")
    global output
    output = Entry(output_frame, width=50)

    output_label.grid(row=0, column=0, columnspan=button_columns)
    output.grid(row=1, column=0, columnspan=button_columns)

    root.mainloop()

if __name__=="__main__":
    main()