from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def main():
    url = "https://www.sgcarmart.com/new_cars/index.php"
    try:
        # 1. open page - input
        page = urlopen(url)  # open the webpage

        # 2. retrieve cars from page with bs4 - process
        cars = retrieve_from_page(page)

        # 3. print the cars - output
        # print_cars()
        for index, car in enumerate(cars):
            print("{:2} ) {}".format(index + 1, car))
    except Exception as ex:
        print(ex)


def retrieve_from_page(page):
    # get BeautifulSoup's html parser to interpret the page
    soup = BeautifulSoup(page, 'html.parser')

    # extract all div tags with class "limittwolines"
    # to put into a list "temp_list"
    temp_list = soup.findAll('div', {"class": "limittwolines"})

    cars = []  # list of cars; initially empty
    for element in temp_list:
        cars.append(element.text)

    cars.sort()  # sort the cars alphabetically
    return cars


main()