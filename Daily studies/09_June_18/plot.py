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


import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot

labels = ["iOS", "Android", "Web", "Reactive Native"]
value = [25, 50, 65, 42]
color = ["green", "white", "yellow", "red"]
explode = [0, 0, 0, 0.2]

pyplot.pie(value, labels = labels, colors = color, explode = explode, shadow = True)
pyplot.axis("equal")

pyplot.show()
