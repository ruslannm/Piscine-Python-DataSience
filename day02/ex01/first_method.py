#!/usr/bin/python3

class Research():
    def file_reader(self):
        filename = 'data.csv'
        try:
            with open(filename, 'r') as f:
                return f.read()
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    print(Research().file_reader())
