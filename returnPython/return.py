def modMult(x, y, mod):
    return x * y % mod

x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
mod = int(input('Enter the modulo that you need for result (num1 * num2 % mod): '))

print(modMult(x, y, mod))