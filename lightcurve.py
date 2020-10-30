import pandas
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# Make sure to check the Magnitude column in the data for > or < signs and remove them
df = pandas.read_csv(r"<filepath>")  # Substitute <filepath> with file path
df.drop_duplicates(subset = "JD", keep = 'first')
plt.scatter(df["JD"], df["Magnitude"],s = 5, c = 'black')
plt.xlabel("Julian Date")
plt.ylabel("Magnitude")
plt.title("Light Curve")
plt.gca().invert_yaxis()
ax = plt.axes()
ax.yaxis.set_major_locator(plt.MaxNLocator(10))
plt.show()

