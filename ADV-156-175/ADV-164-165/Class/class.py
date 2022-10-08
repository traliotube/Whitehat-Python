from cProfile import label
from textwrap import wrap
from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import Combobox

root = Tk()
root.title("Planet Encyclopedia")
root.geometry('700x700')
root.configure(bg="lightblue")

mercury = ImageTk.PhotoImage(Image.open("img/mercury.jpg"))
venus = ImageTk.PhotoImage(Image.open("img/venus.jpg"))
earth = ImageTk.PhotoImage(Image.open("img/earth.jpg"))
mars = ImageTk.PhotoImage(Image.open("img/mars.jpg"))

labelPlanet = Label(root, text="Planet:", bg="lightblue")
labelPlanetName = Label(root, bg="lightblue", font=("courier", 18, "bold"))
imagePlanet = Label(root, bg="gold2", highlightthickness=5,
                    borderwidth=2, relief=SOLID)
labelGravityRadius = Label(root, font=("castellar"), bg="lightblue")
labelPlanetInfo = Label(root, font=("courier", 12, "bold"),
                        bg="lightblue", wraplength=600)

planet = StringVar()
planetsList = ["Mercury", "Venus", "Earth", "Mars"]
dropdown = Combobox(root, values=planetsList, textvariable=planet, state="readonly")
dropdown.current(0)


def planetInfo():
    if planet.get() == "Mercury":
        labelPlanetName["text"] = "Mercury"
        imagePlanet["image"] = mercury
        labelGravityRadius["text"] = " Gravity : 3.7 m/s² \n Radius : 2,439.7 km"
        labelPlanetInfo["text"] = "Mercury is the smallest planet in the Solar System and the closest to the Sun. Its orbit around the Sun takes 87.97 Earth days, the shortest of all the Sun's planets."
    elif planet.get() == "Venus":
        labelPlanetName["text"] = "Venus"
        imagePlanet["image"] = venus
        labelGravityRadius["text"] = " Gravity : 8.87 m/s² \n Radius : 6,051.8 km"
        labelPlanetInfo[
            "text"] = "Venus is the second planet from the Sun, orbiting it every 224.7 Earth days. It has the longest rotation period (243 days) of any planet in the Solar System and rotates in the opposite direction to most other planets."
    elif planet.get() == "Earth":
        labelPlanetName["text"] = "Earth"
        imagePlanet["image"] = earth
        labelGravityRadius["text"] = " Gravity : 9.8 m/s² \n Radius : 6,371.0 km"
        labelPlanetInfo["text"] = "Earth is the third planet from the Sun and the only planet known to have permanently fixed equatorial orbits. It is the densest planet in the Solar System and the only planet in our Solar System with liquid water on the surface."
    elif planet.get() == "Mars":
        labelPlanetName["text"] = "Mars"
        imagePlanet["image"] = mars
        labelGravityRadius["text"] = " Gravity : 3.7 m/s² \n Radius : 3,390.0 km"
        labelPlanetInfo["text"] = "Mars is the fourth planet from the Sun and the second smallest planet in the Solar System after Mercury. In English,Mars is often referred to as the 'Red Planet' because the reddish iron oxide prevalent on its surface gives it a reddish appearance that is distinctive among the astronomical bodies visible to the naked eye."


btn = Button(root, text="Show planet info", command=planetInfo)

labelPlanet.place(relx=0.2, rely=0.1, anchor=CENTER)
dropdown.place(relx=0.5, rely=0.1, anchor=CENTER)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)
labelPlanetName.place(relx=0.5, rely=0.25, anchor=CENTER)
imagePlanet.place(relx=0.5, rely=0.5, anchor=CENTER)
labelGravityRadius.place(relx=0.5, rely=0.69, anchor=CENTER)
labelPlanetInfo.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()
