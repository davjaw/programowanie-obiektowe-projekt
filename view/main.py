import tkinter
from customtkinter import *

root = CTk()

root.title("Python project")
root.geometry("1000x1000")
root.configure(fg_color="#1b243a")
root.resizable(width=False, height=False)

def piecharts():
    CTkCheckBox(root, text="% Ocen w przedziale gatunków").grid(row=2, column=1, padx=(120, 0))
    CTkCheckBox(root, text="% Ocen w przedziale lat").grid(row=2, column=2)
    CTkCheckBox(root, text="% Gatunków w przedziale lat").grid(row=2, column=3)
    CTkCheckBox(root, text="Średnia ocen na każdy gatunek").grid_remove()
    CTkCheckBox(root, text="Srednia ocen na każdy rok").grid_remove()
    CTkCheckBox(root, text="Rozkład procentowy gatunków na kazdy rok").grid_remove()
    CTkCheckBox(root, text="Ilość wszystkich opinii na kazdy rok").grid_remove()
def barcharts():
    CTkCheckBox(root, text="Średnia ocen na każdy gatunek").grid(row=2, column=1, padx=(120, 0))
    CTkCheckBox(root, text="Srednia ocen na każdy rok").grid(row=2, column=2)
    CTkCheckBox(root, text="% Gatunków w przedziale lat").grid_remove()
    CTkCheckBox(root, text="% Ocen w przedziale gatunków").grid_remove()
    CTkCheckBox(root, text="% Ocen w przedziale lat").grid_remove()
    CTkCheckBox(root, text="Rozkład procentowy gatunków na kazdy rok").grid_remove()
    CTkCheckBox(root, text="Ilość wszystkich opinii na kazdy rok").grid_remove()

def pointcharts():
    CTkCheckBox(root, text="Rozkład procentowy gatunków na kazdy rok").grid(row=2, column=1, padx=(120, 0))
    CTkCheckBox(root, text="Ilość wszystkich opinii na kazdy rok").grid(row=2, column=2)
    CTkCheckBox(root, text="% Gatunków w przedziale lat").grid_remove()
    CTkCheckBox(root, text="% Ocen w przedziale gatunków").grid_remove()
    CTkCheckBox(root, text="% Ocen w przedziale lat").grid_remove()
    CTkCheckBox(root, text="Średnia ocen na każdy gatunek").grid_remove()
    CTkCheckBox(root, text="Srednia ocen na każdy rok").grid_remove()



CTkLabel(root, text="imGraphs", text_color="#C0256F", font=("Kaushan Script", 64)).grid(row=0, column=2, pady=(0, 50))
CTkButton(root, text="Kołowy", anchor="center", text_color="white", fg_color="#C0256F", corner_radius=150,
          font=("Quicksand", 20), command=piecharts).grid(row=1, column=1, padx=(225, 0))
CTkButton(root, text="Słupkowy", anchor="center", text_color="white", fg_color="#C0256F", corner_radius=150,
          font=("Quicksand", 20), command=barcharts).grid(row=1, column=2)
CTkButton(root, text="Punktowy", anchor="center", text_color="white", fg_color="#C0256F", corner_radius=150,
          font=("Quicksand", 20), command=pointcharts).grid(row=1, column=3)
root.mainloop()
