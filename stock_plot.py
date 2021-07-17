import matplotlib.pyplot as plt

def main():
    # 1. load the file into 2 lists : dates / prices
    csv_file = "data/SE.csv"
    dates, prices = load_data(csv_file)

    # 2. plot the graph
    plot_graph(dates, prices, "SEA Limited")

    print("End of program")


def plot_graph(dates, prices, stock_title):
    plt.plot(dates, prices)
    plt.title(stock_title)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()


def load_data(filename):
    dates = []
    prices = []

    # process the file here and append to dates and prices
    with open(filename, "r") as in_file:
        in_file.readline()    # throw away the header
        lines = in_file.readlines() # getting all the lines
        for line in lines:
            data = line.split(",")   # convert the line into a list delimited by comma
            current_date = data[0]   # first column
            closing_price = float(data[4])  # 5th column convert to float
            dates.append(current_date)    # add to dates
            prices.append(closing_price)  # add to prices
            # print(data)

    return dates, prices


main()  # call the main program