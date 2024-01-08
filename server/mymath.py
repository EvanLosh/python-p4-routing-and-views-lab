def math(num1, operation, num2):
    num1 = int(num1)
    num2 = int(num2)
    if operation == '+':
        return num1 + num2
    if operation == '-':
        return num1 - num2
    if operation == '*':
        return num1 * num2
    if operation == 'div':
        return num1 / num2
    if operation == '%':
        return num1 % num2
    

print(math('5','+','5'))
