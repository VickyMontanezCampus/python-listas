""" 3. En pocos días comienza la vuelta a España y la federación
colombiana de ciclismo, como incentivo ha determinado pagar
un valor adicional. El programa pedirá por teclado el sueldo
básico por kilometro recorrido, el número de kilómetros
recorridos durante toda la vuelta, numero de kilómetros
recorridos con la camiseta de líder.
Calcular el valor a pagar total, si se sabe que si recorre en la
bici más de 1800 kilómetros con la camiseta de líder, esos
kilómetros se consideran especiales y tendrán un recargo de
25%.
El total de kilómetros por recorrer durante toda la vuelta serán
3.277 kilómetros,el ganador de la vuelta a España recibirá 700
millones de pesos. """

def vuelta():
    ciclista = []
    sueldoBasico = []
    Nkilometros = []
    f = int(input("Cuantos ciclistas desea agregar?: "))
    sueldo= int(input("Digite el sueldo básico: "))
    sueldoBasico.append(sueldo)
    for i in range(f):
        nombre = input("Digite el nombre del ciclista: ")
        ciclista.append(nombre)
        kilom= float(input("Ingrese los kilometros recorridos: "))
        Nkilometros.append(kilom)
        
    return ciclista, sueldoBasico, Nkilometros

def listarCiclistas(ciclista):
    print("Los ciclistas ingresados son: ")
    for i in range(len(ciclista)):
        print(ciclista[i],"con ", Nkilometros[i]," kilometros recorridos")
        print()

def Calcularpaga(ciclista, sueldoBasico, Nkilometros):
    Busca= input("Digite el ciclista que quieres consultar: ")
    for i in range(len(ciclista)):
        if Busca == ciclista[i]:
            l= input("El ciclista tuvo la camisa de lider? (si/no): ")
            if l == "si":
                    kl=int(input("Cuántos kilometros recorrió con la camisa de lider?: "))
                    if kl>1800:
                            sueldoBase = [n * kl for n in sueldoBasico]
                            lsueldo= [s * 1.25 for s in sueldoBase]
                            pos= Busca in ciclista
                            psueldo= []
                            for x in Nkilometros:
                                    for y in sueldoBasico:
                                        psueldo.append(x*y)
                            tsueldo= []
                            for i in psueldo:
                                for a in lsueldo:
                                    tsueldo.append(i+a)
                                    print("El pago especial para el ciclista es ", lsueldo)
                                    print("El pago total para el ciclista es ", tsueldo)
                    elif kl<=1800:
                            pos= Busca in ciclista
                            csueldo = []
                            for x in Nkilometros:
                                for y in sueldoBasico:
                                    csueldo.append(x*y)
                                    print("El pago para el ciclista es ", csueldo)
            elif l== "no":
                    pos= Busca in ciclista
                    usueldo = []
                    for x in Nkilometros:
                        for y in sueldoBasico:
                            usueldo.append(x*y)
                    print("El pago para el ciclista es ", usueldo )

def ganador(ciclista, Nkilometros):
    print("El ciclista campeón es ")
    ciclista.sort()
    pos=max([int(i) for i in Nkilometros])
    x=Nkilometros.index(pos)
    print(f'{ciclista[x]} con {Nkilometros[x]} kilometros recorridos ')
    print("¡GANADOR DE LA VUELTA ESPAÑA!")
    print("¡RECIBE 700 MILLONES!")
        

option = -1
while option != 0:
     
    print("-------M E N U-----")
    print("1. Agregar ciclistas")
    print("2. Informe de los ciclistas")
    print("3. Calcular el valor a pagar")
    print("4. Ganador de la vuelta España")
    option=int(input("Digite la opción que desea: "))

    if option==1:
        ciclista, sueldoBasico, Nkilometros = vuelta()
    elif(option == 2):
        listarCiclistas(ciclista)
    elif(option == 3):
        Calcularpaga(ciclista, sueldoBasico, Nkilometros)
    elif(option == 4):
        ganador(ciclista, Nkilometros)
        
