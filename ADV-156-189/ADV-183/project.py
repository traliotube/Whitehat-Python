from tkinter import *
import requests
import json

root = Tk()
root.title("Capital City Info")
root.geometry("350x500")
root.configure(background="white")


cityLabel = Label(root, text="Capital City Name", font=(
    "Helvetica", 18, 'bold'), bg="white")
entry = Entry(root)
countryLabel = Label(root, text="Country: ", bg="white", font=("bold", 10))
regionLabel = Label(root, text="Continent: ", bg="white", font=("bold", 10))
languageLabel = Label(root, text="Language: ",
                      bg="white", font=("bold", 10))
populationLabel = Label(root, text="Population: ",
                        bg="white", font=("bold", 10))
areaLabel = Label(root, text="Area: ", bg="white", font=("bold", 10))

cityLabel.place(relx=0.5, rely=0.1, anchor=CENTER)
entry.place(relx=0.5, rely=0.2, anchor=CENTER)
countryLabel.place(relx=0.5, rely=0.4, anchor=CENTER)
regionLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
languageLabel.place(relx=0.5, rely=0.6, anchor=CENTER)
populationLabel.place(relx=0.5, rely=0.7, anchor=CENTER)
areaLabel.place(relx=0.5, rely=0.8, anchor=CENTER)


def send():
    apiRequest = requests.get(
        f"https://restcountries.com/v2/capital/{entry.get()}")
    outputJson = json.loads(apiRequest.content)

    countryLabel["text"] = "Country: " + outputJson[0]["name"]
    regionLabel["text"] = "Continent: " + outputJson[0]["subregion"]
    languageLabel["text"] = "Language: " + \
        outputJson[0]["languages"][0]["name"]
    populationLabel["text"] = "Population: " + \
        "{:,}".format(outputJson[0]["population"])
    areaLabel["text"] = "Area: " + \
        "{:,}".format(round(outputJson[0]["area"])) + " sq.km"
    cityLabel["text"] = entry.get()

    entry.destroy()
    btn.destroy()


btn = Button(root, text="Get Details", command=send, relief=FLAT)
btn.place(relx=0.5, rely=0.3, anchor=CENTER)

root.mainloop()
