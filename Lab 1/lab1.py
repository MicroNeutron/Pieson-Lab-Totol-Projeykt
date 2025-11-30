def greet_user():
    print("=== Welcome to the Multi-function Program! ===")
    
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    
    print(f"\nHello {name}! Nice to meet you.")
    print(f"You are {age} years old. Welcome to our program!")

def simple_calculator():
    print("\n" + "="*50)
    print("=== SIMPLE CALCULATOR ===")
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        sum_result = num1 + num2
        difference_result = num1 - num2
        product_result = num1 * num2
        
        print(f"\nCalculation Results:")
        print(f"{num1} + {num2} = {sum_result}")
        print(f"{num1} - {num2} = {difference_result}")
        print(f"{num1} × {num2} = {product_result}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")

def temperature_converter():
    print("\n" + "="*50)
    print("=== TEMPERATURE CONVERTER ===")
    
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        
        fahrenheit = (celsius * 9/5) + 32
        
        print(f"\n{celsius}°C is equal to {fahrenheit:.2f}°F")
        
        if fahrenheit < 32:
            print("That's freezing cold! ❄️")
        elif fahrenheit < 50:
            print("That's quite chilly! 🧥")
        elif fahrenheit < 70:
            print("That's pleasant weather! 🌤️")
        elif fahrenheit < 90:
            print("That's warm! ☀️")
        else:
            print("That's really hot! 🔥")
            
    except ValueError:
        print("Error: Please enter a valid temperature!")

def main():
    greet_user()
    simple_calculator()
    temperature_converter()
    
    print("\n" + "="*50)
    print("Thank you for using our multi-function program!")
    print("="*50)

if __name__ == "__main__":
    main()