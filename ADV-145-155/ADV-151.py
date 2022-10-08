months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")
profits = (218983, 207077, 306519, 135127, 477549, 262648,
           397945, 475812, 197306, 154309, 481541, 419896)

maxProfitNumber = max(profits)
maxProfitIndex = profits.index(maxProfitNumber)
maxProfixMonth = months[maxProfitIndex]
print(
    f"The month with the highest profit is {maxProfixMonth} with {maxProfitNumber}. The index is {maxProfitIndex}.")

minProfitNumber = min(profits)
minProfitIndex = profits.index(minProfitNumber)
minProfixMonth = months[minProfitIndex]
print(
    f"The month with the lowest profit is {minProfixMonth} with {minProfitNumber}. The index is {minProfitIndex}.")
