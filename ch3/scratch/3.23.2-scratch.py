from matplotlib import pyplot

# pyplot.plot([1, 2, 3, 4, 5], [1.1, 10.0, 25.4, 44.5, 61.0])
# pyplot.plot([1, 2, 3, 4, 5], [1.1, 10.0, 25.4, 44.5, 61.0])  # Highs
pyplot.plot([1, 2, 3, 4, 5], [1.1, 10.0, 25.4, 44.5, 61.0], "r--o")
pyplot.plot([1, 2, 3, 4, 5], [-16.9, -12.7, -2.5, 20.6, 37.8])  # Lows

pyplot.xlim(0.5, 5.5)
pyplot.ylim(-40, 100)

pyplot.title("Average Temperatures in Fairbanks")
pyplot.xlabel("Month")
pyplot.ylabel("Temperature")

pyplot.legend(["High", "Low"])

pyplot.xticks(
   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
   ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

pyplot.grid(True)

pyplot.show()
