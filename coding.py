#Question 1
def add(a, b): 
    return a + b

def substract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

try:
    while True:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
        choice = input('Choose operation (+, -, *, /) or \'exit\' to quit: ')

        if choice == '+':
            print(add(num1, num2))
        elif choice == '-':
            print(substract(num1, num2))
        elif choice == '*':
            print(multiply(num1, num2))
        elif choice == '/':
            print(divide(num1, num2))
        elif choice == 'exit':
            break
        else:
            pass
except ValueError as e:
    print('Error:', e)

except ZeroDivisionError as e:
    print('Error:', e)




#Question 2
while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break        # break out of loop
    
    num = int(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")





#Question3
while True:
    age = input("Enter your age (or type exit to quit): ")
    if age == 'exit':
        print("Goodbye!")
        break
    
    try:
        age = int(age)
        if age >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except ValueError:
        print("Invalid input. Please enter a number.")