enunciado="""Bienvenido, por favor seleccione la opción que desea:
1. Convertir Millas a Kilometros
2. Convertir Kilometros a Millas
"""
def conv():
    a=int(input(enunciado))
    k=1.609
    mi=0.60214
    if a==1:
        m=float(input("Por favor ingrese el número de Millas que desea convertir a Kilometros: "))
        km=k*m
        km=round(km,4)
        print(str(m) + ' millas, equivale a ' + str(km) + ' kilometros')
    elif a==2:
        km=float(input("Por favor ingrese el número de Kilometros que desea convertir a millas: "))
        m=mi*km
        m=round(m,4)
        print(str(km) + ' 2Kilometros, equivale a ' + str(m) + ' Millas')
    else:
        print('No escribio un numero valido')

def main():
    conv()

if __name__ == '__main__':
    main()