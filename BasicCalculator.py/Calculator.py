num1 = int(input('Enter the first number! '))
num2 = int(input('Enter the second number! '))

operator = input('Enter the operation you want to use(+, -, /, *, **, %) ')

result = 0
ok = True
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
elif operator == '**':
    result = num1 ** num2
elif operator == '%':
    result = num1 % num2
else:
    ok = False

print('The result is ', result, '!') if ok == True else print('Invalid Operator! ')
