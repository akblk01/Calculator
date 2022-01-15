def calculate(numOne, numTwo, process):
    
    if process not in "+-*/q":
        print("Invalid operation\n")
    elif process == "+":
        return print(f"{numOne} + {numTwo} = {numTwo+numOne}")
    elif process == "-":
        return print(f"{numOne} - {numTwo} = {numTwo-numOne}")
    elif process == "*":
        return print(f"{numOne} * {numTwo} = {numTwo*numOne}")
    elif process == "/":
        return print(f"{numOne} / {numTwo} = {numTwo/numOne}")

while True:
    try:
        process = input("Press 'q' to exit.\nSelect the action you want to perform (' +, -, *, / '): ")
        if process == "q":
            print("Exiting the calculator.")
            break
        numOne = int(input("Enter the first number: "))
        numTwo = int(input("Enter the second number: "))
        calculate(numOne,numTwo,process)
    except:
        print("Please enter a numeric value.\n")