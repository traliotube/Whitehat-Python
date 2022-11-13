from stringprep import c9_set
from tkinter import *
import requests
import json

root = Tk()
root.title("My Weather App")
root.geometry("350x300")
root.configure(background="white")
root.overrideredirect(True)


cityLabel = Label(root, text="City Name", font=(
    "Helvetica", 18, 'bold'), bg="white")
entry = Entry(root)
weatherLabel = Label(root, text="Weather: ", bg="white", font=("bold", 10))
humidityLabel = Label(root, text="Humidity: ", bg="white", font=("bold", 10))
tempLabel = Label(root, text="Temperature: ",
                  bg="white", font=("bold", 10))

cityLabel.place(relx=0.5, rely=0.15, anchor=CENTER)
entry.place(relx=0.5, rely=0.35, anchor=CENTER)
weatherLabel.place(relx=0.5, rely=0.6, anchor=CENTER)
humidityLabel.place(relx=0.5, rely=0.7, anchor=CENTER)
tempLabel.place(relx=0.5, rely=0.8, anchor=CENTER)


def send():
    apiRequest = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={entry.get()}&appid=21cab08deb7b27f4c2b55f3e2df28ea4")
    outputJson = json.loads(apiRequest.content)

    weatherLabel["text"] = "Weather: " + \
        outputJson["weather"][0]["description"]
    humidityLabel["text"] = "Humidity: " + str(outputJson["main"]["humidity"])
    tempLabel["text"] = "Temperature: " + \
        str(round(outputJson["main"]["temp_max"]-273.15, 2))
    cityLabel["text"] = entry.get()

    entry.destroy()
    btn.destroy()


btn = Button(root, text="Search", command=send, relief=FLAT)
btn.place(relx=0.5, rely=0.48, anchor=CENTER)

root.mainloop()
