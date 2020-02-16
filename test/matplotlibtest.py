import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
def getData(i):
    temps = []
    for i in range(50):
        temps.append(random.random())
    axis.clear()
    axis.plot(temps)
graph = plt.figure()
axis = graph.add_subplot(1,1,1)
ani = animation.FuncAnimation(graph,getData,1000)
plt.show()