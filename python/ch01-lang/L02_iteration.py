def main():

    print("Python iteration demo")

    #while True:
        #name = input("What is your name? ")
        #if not name:
            #break

        #print(f"Nice to meet you {name}.")

    nums = [1, 5, 6, 7, 10, 2]  #<__ List<object>
    for n in nums:
        print(f"The next number is {n}.")

    for idx, n in enumerate(nums, start=1):
        print(f"{idx}the number is {n}.")


if __name__ == '__main__':
    main()

