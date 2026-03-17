import matplotlib.pyplot as plt

data = [10, 20, 20, 30, 30, 30, 40, 50]

plt.hist(data, bins=5, color='purple')
plt.title("Histogram Example")

plt.show()