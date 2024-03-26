""" 
Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""

from tkinter import ttk, Tk
from poke_api import get_pokemon_info

# Create the main window
root = Tk()
root.title("Pokemon Information")

# TODO: Create the frames
inp = ttk.Frame(root)
inp.grid(row=0, column=0, columnspan=2)

inf = ttk.LabelFrame(root, text="Info")
inf.grid(row=1, column=0)

stat = ttk.LabelFrame(root, text="Stats")
stat.grid(row=1, column=1)

def get_info():
    pok_name = inp_ent.get().strip()
    if not pok_name:
       return
    
    pok_info = get_pokemon_info(pok_name)

    if pok_info:
        heig_val["text"] = pok_info["height"]
        weig_val["text"] = pok_info["weight"]



        hp_bar["value"] = pok_info["stats"][0]["base_stat"]
        attak_bar["value"] = pok_info["stats"][1]["base_stat"]
        defe_bar["value"] = pok_info["stats"][2]["base_stat"]


    return


# TODO: Populate the user input frame with widgets
inp_labl = ttk.Label(inp, text="Pokemon Name:")
inp_labl.grid(row=0, column=0)

inp_ent = ttk.Entry(inp)
inp_ent.grid(row=0, column=1)

inp_buttn = ttk.Button(inp, text="Get Info", command=get_info)
inp_buttn.grid(row=0, column=2)



# Populate the Info frame

hight_labl = ttk.Label(inf, text="Height:")
hight_labl.grid(row=0, column=0)

weigt_labl = ttk.Label(inf, text="Weight:")
weigt_labl.grid(row=1, column=0)

typ_labl = ttk.Label(inf, text="Type:")
typ_labl.grid(row=2, column=0)

heig_val = ttk.Label(inf)
heig_val.grid(row=0, column=1)

weig_val = ttk.Label(inf)
weig_val.grid(row=1, column=1)

type_val = ttk.Label(inf)
type_val.grid(row=2, column=1)

#populate the Stats frame

hp_labl = ttk.Label(stat, text="HP:")
hp_labl.grid(row=0, column=0)

attak_labl = ttk.Label(stat, text="Attack:")
attak_labl.grid(row=1, column=0)

def_labl = ttk.Label(stat, text="Defense:")
def_labl.grid(row=2, column=0)

spattak_labl = ttk.Label(stat, text="Special Attack:")


spdef_labl = ttk.Label(stat, text="Special Defense:")


speed_labl = ttk.Label(stat, text="Speed:")



Max_Stat = 255

hp_bar = ttk.Progressbar(stat, maximum=Max_Stat)


attak_bar = ttk.Progressbar(stat, maximum=Max_Stat)


defe_bar = ttk.Progressbar(stat, maximum=Max_Stat)


spatak_bar = ttk.Progressbar(stat, maximum=Max_Stat)


spdef_bar = ttk.Progressbar(stat, maximum=Max_Stat)


speed_bar = ttk.Progressbar(stat, maximum=Max_Stat)



# TODO: Define button click event handler function

root.mainloop()
