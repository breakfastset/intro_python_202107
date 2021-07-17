import matplotlib.pyplot as plt

x_values = [ 5, 7, 10, 15, 21 ]
y_values = [ 22, 55, 77, 101, 200]

plt.plot(x_values, y_values)    # plotting y against x (line chart)
plt.scatter(x_values, y_values)   # scatter plot
plt.bar(x_values, y_values)

plt.xlabel("Days")
plt.ylabel("Savings")
plt.title("Savings in February")
plt.show()