#!/usr/bin/python3
import sys

def put_name_price():
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
    len_argv = len(argv)
    if len_argv == 2:
        company_key = None
        for k, v in companies.items():
            if v.lower() == argv[1].lower():
                company_key = v
                break
        if company_key:
            price = stocks.get(company_key)
            if price:
                print(k, price)
            else:
                print('Unknown ticker')
        else:
            print('Unknown ticker')


if __name__ == "__main__":
    put_name_price()