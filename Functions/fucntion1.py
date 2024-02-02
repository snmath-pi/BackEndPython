def greetingsFunction(name, gender):
    print('Hello! How are you', 'Mr.' if gender == 'M' else 'Ms.', name)

gender = input('Enter you Gender(F / M): ')
name = input('Enter you name: ')
greetingsFunction(name, gender)

def multiNmaes(*names):
    print('Welcome', names)
    
multiNmaes('Saksham', 'Negi', 'Tim', 'Uler')