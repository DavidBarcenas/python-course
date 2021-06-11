objetive = int(input('Write a number: '))
epsilon = 0.01
low = 0.0
high = max(1.0, objetive)
response = (high + low) / 2

while abs(response**2 - objetive) >= epsilon:
    if response**2 < objetive:
        low = response
    else:
        high = response

    response = (high + low) / 2

print(f'La raiz cuadrada de {objetive} es {response}')