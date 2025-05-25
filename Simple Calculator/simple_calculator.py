#Calculator Program that perform only basic arithematic Operations
#Function to perform Addition.
def add(a,b):
    return a + b
#Function to perform Subtraction.
def subtract(a,b):
    return a - b
#Function to perform Multiplication.
def multiply(a,b):
    return a * b
#Function to perform Division.
def division(a,b):
    if b==0:
        raise ValueError("Error: Division by zero is not allowed")
    
    return a / b
# Operations List 
def calculator():
    print("Calculator Operations List")
    print("Enter 1 - Addition ")
    print("Enter 2 - Subtraction ")
    print("Enter 3 - Multiplication ")
    print("Enter 4 - Division ")

    try:
        #Get user inputs
        num1=float(input("Enter First Number: "))
        num2=float(input("Enter Second Number: "))
        Operation=input("Select Operation (1-4): ")
        # Perform calculator based on operation  
        if Operation == '1':
            result = add(num1,num2)
            print(f'{num1} + {num2} = {result}')
        elif Operation == '2':
            result = subtract(num1,num2)
            print(f'{num1} - {num2} = {result}') 
        elif Operation == '3':
            result= multiply(num1,num2)
            print(f'{num1} * {num2} = {result}')
        elif Operation == '4':
            result= division(num1,num2)
            print(f'{num1} / {num2} = {result}')
        else:
            print("Error: Invalid Operation Selected")
    except ValueError as e:
        if str(e).startswith("Error"):
            print(e)
        else:
            print("Error: Please Enter Valid Numbers!")
    except Exception as e:
        print(f'Error Occurred: {e}')

if __name__ == "__main__":
    calculator()