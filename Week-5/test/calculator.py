def main():
    x = int(input("Wat is x? "))
    print("x in het kwadraat is", square(x))

def square(number):
    return number * number

if __name__ == "__main__":
    main()