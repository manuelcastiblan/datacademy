#Este es el reto número 4 propuestos por platzi para Datacademy, en este resto se propone realizar un script que pueda calcular el volumen de distintas ficugras geometricas
pi=3.14
enunciado="""Bienvenido, por favor seleccione la opción que desee
1. Calcular el volumen de un cilindro 
2. Calcular el volumen de una esfera
3. Calcular el volumen de un cono
"""
def cilindro():
    radio=float(input("Por favor digite el radio del cilindro: "))
    altura=float(input("Por favor digite la altura del cilindro: "))
    volumen=(pi)*(radio**2)*(altura)
    volumen=round(volumen,3)
    print(" El volumen del clindro es: " +str(volumen))

def esfera():
    radio=float(input("Por favor digite el radio de la esfera: "))
    volumen=((pi)*(4)*(radio**3))/3
    volumen=round(volumen,3)
    print(" El volumen de la esfera es: " +str(volumen))

def cono():
    radio=float(input("Por favor digite el radio del cono: "))
    altura=float(input("Por favor digite la altura del cono: "))
    volumen=((pi)*(radio**2)*(altura))/3
    volumen=round(volumen,3)
    print(" El volumen del cono es: " +str(volumen))

def main():
    e=int(input(enunciado))
    if e==1:
        cilindro()
    elif e==2:
        esfera()
    elif e==3:
        cono()
    else:
        print('No selecciono una opción válida')    

if __name__ == '__main__':
    main()