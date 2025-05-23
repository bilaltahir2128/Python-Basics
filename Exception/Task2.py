try:
    x = int(input("Enter a number: "))  
    result = 10 / x  
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You can't divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")
finally:
    print("Execution complete.")