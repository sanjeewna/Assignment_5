def main():
    numbers = []
    while True:
        user_input = input("Enter a number (or press Enter to quit): ")
        if user_input == '':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number.")

    # Sort the numbers in descending order
    numbers.sort(reverse=True)

    # Print the five greatest numbers
    print("The five greatest numbers are:")
    for i in range(min(5, len(numbers))):
        print(numbers[i])

if __name__ == "__main__":
    main()
