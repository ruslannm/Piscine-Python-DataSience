#!/usr/bin/python3

class Must_read():
    filename = 'data.csv'
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    Must_read()
