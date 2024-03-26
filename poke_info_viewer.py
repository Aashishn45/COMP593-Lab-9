""" 
Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""

from tkinter import ttk, Tk

# Create the main window
root = Tk()
root.title("Pokemon Information")

# TODO: Create the frames
inp = ttk.Frame(root)
inp.grid(row=0, column=0)

inf = ttk.LabelFrame(root, text="Info")
inf.grid(row=1, column=0)

stat = ttk.LabelFrame(root, text="Stats")
stat.grid(row=1, column=1)



# TODO: Populate the user input frame with widgets
inp_labl = ttk.Label(inp, text="Pokemon Name:")
inp_labl.grid(row=0, column=0)





# TODO: Define button click event handler function

root.mainloop()