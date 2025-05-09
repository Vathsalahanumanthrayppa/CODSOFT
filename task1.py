def main():
    # Prompt user for the first number
    num1 = float(input("Enter the first number: "))
    
    # Prompt user for the second number
    num2 = float(input("Enter the second number: "))
    
    # Display operation choices
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # Prompt user for the operation
    choice = input("Enter the number corresponding to the operation (1/2/3/4): ")
    
    # Perform calculation based on user choice
    if choice == '1':
        result = num1 + num2
        operation = '+'
    elif choice == '2':
        result = num1 - num2
        operation = '-'
    elif choice == '3':
        result = num1 * num2
        operation = '*'
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            operation = '/'
        else:
            print("Error: Cannot divide by zero.")
            return
    else:
        print("Invalid choice.")
        return
    
    # Display the result
    print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()