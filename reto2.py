#Este es el reto número dos de Datacademy de platzi, este es un juego de piedra papel o tijera
enunciado="""Este es un juego de piedra, papel o tijera, el ganador será el que gane dos de tres rondas
Selecciona una de las 3 opciones:
1. Piedra
2. Papel
3. Tijera
"""
def juego():
    contador=1
    victoria1=0
    victoria2=0
    while contador <=3:
        jugador1=int(input(enunciado))
        jugador2=int(input(enunciado))
        if (jugador1==1 and jugador2==2) or (jugador1==2 and jugador2==3) or (jugador1==3 and jugador2==1):
            print("El ganador es el jugador 2")
            victoria1+=1
            if victoria1 ==2:
                print("El jugador 2 gano dos de tres rondas")  
                break
            else:   
                contador+=1      
        elif (jugador1==1 and jugador2==3) or(jugador1== 2 and jugador2==1) or (jugador1==3 and jugador2==2):
            print("El ganador es el jugador 1")
            victoria2+=1
            if victoria2 ==2:
                print("El jugador 1 gano dos de tres rondas")  
                break
            else:   
                contador+=1  
        else:
            print('Ningun jugador ha ganado')
    
def main():
    juego()

if __name__ == '__main__':
    main()