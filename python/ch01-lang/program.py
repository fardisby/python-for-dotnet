def main():
    name = input("Enter Your Name?")
    some_methode(name)


def some_methode(name):
    if name.strip().lower() == 'fardis':
        print("Hello")
    else:
        print(f"Nice to meet you {name}.")
        print("My name is python.")


if __name__ == '__main__':
    main()
