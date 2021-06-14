#!/usr/bin/python3
import sys

def get_dict_value(d, search_key):
    search_key = search_key.lower()
    for key, value in d.items():
        if key.lower() == search_key:
            return value
    return None


def get_dict_key(d, search_value):
    search_value = search_value.lower()
    for key, value in d.items():
        if value.lower() == search_value:
            return key
    return None

def check_commas(search_list):
    for search_str in search_list:
        search_str = search_str.strip().split()
        if search_str == []:
            return 1
    return 0


def put_info():
    companies = {
        'Apple' : 'AAPL',
        'Microsoft' : 'MSFT',
        'Netflix' : 'NFLX',
        'Tesla' : 'TSLA',
        'Nokia' : 'NOK'
        }
    stocks = {
        'AAPL' : 287.73,
        'MSFT' : 173.79,
        'NFLX' : 416.90,
        'TSLA' : 724.88,
        'NOK' : 3.37
        }
    argv = sys.argv
    if len(argv) == 2:
        search_list = argv[1].strip().split(',')
        if check_commas(search_list):
            return 1
        for search_str in search_list:
            search_str = search_str.strip().split()
            search_str = ' '.join(search_str)
            if search_str:
                ticker = get_dict_value(companies, search_str)
                if ticker:
                    company = get_dict_key(companies, ticker)
                    price = get_dict_value(stocks, ticker)
                    if price:
                        print('{} stock price is {}'.format(company, price))
                else:
                    company = get_dict_key(companies, search_str)
                    if company:
                        ticker = get_dict_value(companies, company)
                        print('{} is a ticker symbol for {}'.format(ticker, company))
                    else:
                        print('{} is an unknown company or an unknown ticker symbol'.format(search_str))


if __name__ == "__main__":
    put_info()
