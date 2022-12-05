import matplotlib.pyplot as plt

plt.close()

days = [1,2,3,4,5,6]
temps = [23.5, 25.5, 23.7, 21.3, 23.1, 24.0]
sizes = [23.5, 25.5, 23.7, 21.3, 23.1, 24.0]
plt.scatter(x=days, y=temps, s=sizes)

plt.show()
