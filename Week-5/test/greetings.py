def main():
    hello('world')
    goodbye('world')


def hello(name = "Guest"):
    print("Hello, " + name)

def goodbye(name = "Guest"):
    print("Goodbye, " + name)

if __name__ == "__main__":
    main()