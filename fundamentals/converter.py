menu = """
Welcome to the currency converter!

1 - Mexican pesos
2 - Argentine pesos 
3 - Colombian pesos

Select an option: """

option = input(menu)

if option == '1':
    pesos = input('How many mexican pesos do you have? ')
    pesos = float(pesos)

    dollar_value = 19.83;

    dollars = pesos / dollar_value;
    dollars = round(dollars, 2)
    dollars = str(dollars)

    print('You have $' + dollars + ' dollars')
elif option == '2':
    pesos = input('How many argentine pesos do you have? ')
    pesos = float(pesos)

    dollar_value = 64

    dollars = pesos / dollar_value;
    dollars = round(dollars, 2)
    dollars = str(dollars)

    print('You have $' + dollars + ' dollars')
elif option == '3':
    pesos = input('How many colombian pesos do you have? ')
    pesos = float(pesos)

    dollar_value = 3875;

    dollars = pesos / dollar_value;
    dollars = round(dollars, 2)
    dollars = str(dollars)

    print('You have $' + dollars + ' dollars')
else:
    print('Ingrese una opcion correcta')