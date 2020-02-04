def basic_error():
    while True:
        try:
            x = int(input("Insert number: "))
            break
        except ValueError:
            print("It is not a number. Insert again.")


if __name__ == "__main__":
    basic_error()
    