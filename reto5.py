#Este es el quinto reto de los correspondientes a la semana 1 propuestos por platzi en su datacademy

def rangos():
    contador =1
    while contador <= 10:
        inf=int(input('Por favor digite el limite inferior: '))
        sup=int(input('Por favor digite el limite superior: '))
        comp=int(input('Por favor digite el número de comparación: '))
        if comp>=inf and comp<=sup:
            print(str(comp) + " Se encuentra dentro del rango")
            break
        elif comp < inf: 
            print(str(comp) + " Se encuentra por debajo del limite inferior")
            contador+=1
        else:
            print(str(comp) + " Se encuentra por encima del limite superior ")
            contador+=1
        
def main():
    rangos()

if __name__ == '__main__':
    main()
    