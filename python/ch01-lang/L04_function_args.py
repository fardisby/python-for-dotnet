def main():
    print("say hello()")
    print()

    print("say_hello(name, times)")
    say_hello("Zoe", 5)
    print()

    print("say_hello(name, times, 1, 2, 3, 4)")
    say_hello("Zoe", 5, 1, 2, 3, 4)
    print()

def say_hello(name='friend', times=1, *args):
    print(f"Hello {name} with times={times}, args={args}!")

if __name__ == '__main__':
    main()