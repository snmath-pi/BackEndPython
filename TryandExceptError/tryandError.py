try:
    x = int(input('Enter a number'))
    print(x)
except ValueError:
    print('This is not an Integer')
else:
    print('Nothing went Wrong')