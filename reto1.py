def triangulo():
    # Altura y base como variables de entrada para el cálculo del area de los triangulos
    base = float(input("Por favor ingresa la base del triangulo: "))
    altura = float(input("Por favor ingresa la altura del triangulo: "))
    # Calculo del area
    area = (base*altura)/2
    area = round(area, 2)
    print('el área del triangulo es: ' + str(area))

    #identificar que tipo de triangulo es

    a=float(input('Por favor ingrese el lado a del triangulo: '))
    b=float(input('Por favor ingrese el lado b del triangulo: '))

    if base == a and base == b:
            print('El triangulo es equilatero')
    elif base == a or base == b:
            print('El triangulo es isósceles')
    else:
            print('El triangulo es escaleno')

def main():
    triangulo()
   

if __name__ == '__main__':
    main()