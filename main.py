def mult(x, y):
    return x * y

def div(x, y):
    return x / y

def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def main():
    operators = ["*", "/", "+", "-"]
    x = int(input("Enter your first number: "))
    y = int(input("Enter your second number: "))
    operator = input("Enter your operator: ")
    if operator not in operators:
        raise Exception("not a proper operator and or digit try again")
    match operator:
        case "*":
            result = mult(x, y)
        case "/":
            result = div(x, y)
        case "+":
            result = add(x, y)
        case "-":
            result = minus(x, y)
    print(result)
    
while True:
    main()
