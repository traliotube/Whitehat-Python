import matplotlib.pyplot as plt
import psutil as p

names = []
percentages = []
count = 0

for process in p.process_iter():
    count += 1
    if count <= 6:
        name = process.name()
        percentage = p.cpu_percent()
        print(f"Name: {name}, Percentage: {percentage}")
        names.append(name)
        percentages.append(percentage)

maxKey = max(percentages)
minKey = min(percentages)
nameList = [names[percentages.index(maxKey)], names[percentages.index(minKey)]]
percentageList = [maxKey, minKey]


plt.figure(figsize=(15, 7))
plt.xlabel("Process Name")
plt.ylabel("CPU Usage")
plt.bar(nameList, percentageList, width=0.6, color=(
    "purple", "green", "red", "blue", "orange", "pink"))
plt.show()
