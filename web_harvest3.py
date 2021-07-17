from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
from operator import itemgetter

ssl._create_default_https_context = ssl._create_unverified_context


def main():
    url = "https://www.sgcarmart.com/new_cars/index.php"
    try:
        # 1. open page - input
        page = urlopen(url)  # open the webpage

        # 2. retrieve cars from page with bs4 - process
        cars = retrieve_from_page(page)

        # 3. print the cars - output
        print_cars(cars)

    except Exception as ex:
        print(ex)


def print_cars(cars):
    for index, car in enumerate(cars):   # car is a list  -> cars is a list of lists
        car_name = car[0]     # extract string name from column 0
        price = car[1]        # extract floating price from column 1
        print("{:2}) {:46} - ${:,.0f}".format(index+1, car_name, price))
        # {:2} means 2 spaces
        # {:.0f} means display float with no decimal places

def retrieve_from_page(page):
    # get BeautifulSoup's html parser to interpret the page
    soup = BeautifulSoup(page, 'html.parser')

    # extract all div tags with class "limittwolines" to put into a list "temp_list"
    #             div tags with class font_black goes into price_list
    temp_list = soup.findAll('div', {"class": "limittwolines"})
    price_list = soup.findAll('div', {"class": "font_black"})

    cars = []  # list of cars; initially empty

    for i in range(len(temp_list)):
        car_name = temp_list[i].text
        price = price_list[i].text  # price is currently text only
        price = price[1:]  # strip off the first character
        price = price.replace(",", "")  # strip off  commas
        price = float(price)   # convert to a number
        car = [car_name, price]    # build a list which includes the name and price of car
        cars.append(car)   # add car to the cars list - becomes a list of lists

    cars.sort(key=itemgetter(1))  # sort the cars list based on price
    return cars


main()