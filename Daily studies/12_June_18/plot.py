# import matplotlib
# matplotlib.use("TkAgg")

# from matplotlib import pyplot

# # 1. Prepare data
# labels = ["iOS", "Android", "Web", "React Native"]
# values = [20, 15, 40, 25]
# colors = ["red", "green", "gray", "purple"]
# explode = [0, 0, 0, 0.2]

# # 2. Plot
# pyplot.pie(values, labels = labels, colors = colors, explode = explode, shadow = True)
# pyplot.axis("equal")


# # 3. Show
# pyplot.show()


Matplotlib in Python

import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot

1. Prepare data
labels = ["iOS", "Android", "Web", "Reactive native"]
values = [20, 15, 40, 25]
colors = ["red", "blue", "black", "yellow"]
explode = [ 0, 0, 0, 0.2]

2. Draw (plot)
pyplot.pie(values,labels = labels, colors = colors, explode = explode, shadow = True)
pyplot.axis("equal")

3. Show
pyplot.show()

Lưu string 