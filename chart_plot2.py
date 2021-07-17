import matplotlib.pyplot as plt

x_values = [ 5, 7, 10, 15, 21 ]
y_values = [ 22, 55, 77, 101, 200]

# plot a 2 x 2 subplot graph that holds 4 items
#   -----------
#   | 1  |  2 |
#   ----------
#  | 3  |  4 |
#  ----------

# plot this on plot 1 (North West)
plt.subplot(221)    # 2 rows, 2 columns, 1st plot
plt.plot(x_values, y_values)    # plotting y against x (line chart)
plt.xlabel("X")
plt.ylabel("Y")

# plot this on plot 2 (North East)
plt.subplot(222)    # 2 rows, 2 columns, 2nd plot
plt.scatter(x_values, y_values)   # scatter plot

# plot this on plot 4 (South East)
plt.subplot(224)    # 2 rows, 2 columns 4th plot
plt.bar(x_values, y_values)

plt.xlabel("Days")
plt.ylabel("Savings")
plt.show()