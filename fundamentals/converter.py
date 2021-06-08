menu = """
Welcome to the currency converter!

1 - Mexican pesos
2 - Argentine pesos 
3 - Colombian pesos

Select an option: """

option = input(menu)

def converter(type_currency, dollar_value):
    pesos = input('How many ' + type_currency + ' pesos do you have? ')
    pesos = float(pesos)
    dollars = pesos / dollar_value;
    dollars = round(dollars, 2)
    dollars = str(dollars)

    print('You have $' + dollars + ' dollars')

if option == '1':
    converter('mexican', 19.83)
elif option == '2':
    converter('argentine', 64)
elif option == '3':
    converter('argentine', 3875)
else:
    print('Ingrese una opcion correcta')