import pandas as pd

data = pd.read_csv("G:\Whitehat Jr\Anaconda Python\ADV-C191\Class\sorted.csv")
data = data.sort_values(by=["Power (Watts)"])
data.to_csv("sortednew.csv", index=False)
