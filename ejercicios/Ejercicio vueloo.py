import numpy as np
from numpy.testing._private.utils import decorate_methods
ruts=np.empty([7, 6], dtype=np.dtype('U100'))
nombres=np.empty([7, 6], dtype=np.dtype('U100'))
telefonos=np.empty([7, 6], dtype=np.dtype('U100'))
asientos= np.array([
                ["1", "2", "3", "4", "5", "6"],
                ["7", "8", "9", "10", "11", "12"],
                ["13", "14", "15", "16", "17", "18"],
                ["19", "20", "21", "22", "23", "24"],
                ["25", "26", "27", "28", "29", "30"],
                ["31", "32", "33", "34", "35", "36"],
                ["37", "38", "39", "40", "41", "42"],
                ])
op=0
while op!=5:
    op=0
    print("Bienvenido al sistema de vuelos Duoc")
    print("-"*50)
    print('''1). Ver asientos disponibles
2) Comprar asiento
3) Anular vuelo
4) Modificar datos de pasajero
5) Salir''')
    while op<1 or 5<op:
        try:
            op=int(input("Ingrese su opcion: "))
        except:
            print("Opcion debe ser un numero")
        if op<1 or 5<op:
            print("Rango de opcion no valido")
    if op==1:
        print(f"Asientos disponibles, 'X'= ocupado\n{asientos[:]}")
        print(f"lista de nombres: \n{nombres[:]}")
        print(f"Lista de ruts: \n{ruts[:]}")
        print(f" Lista de telefonos\n{telefonos[:]}")
    elif op==2:
        rut=input("ingrese su rut sin comas ni guion: ")
        nomb=input("Ingrese su nombre: ")
        telefon=input("ingrese su telefono: ")
        while True:
            print("seleccione el asiento que desea comprar")
            try:
                select=int(input(""))
                break
            except:
                print("Ingrese un numero")
        
        if 43>select and select>=1:
            selstr=str(select)
            for m in range(7):
                for n in range(6):
                    if asientos[m][n]==selstr:
                        asientos[m][n]="X"
                        nombres[m][n]=nomb
                        ruts[m][n]=rut
                        telefonos[m][n]=telefon
            if select>30:
                print("Asiento vip seleccionado, valor: 240.000$")
                precio=240000
            else:
                print("Asiento normal seleccionado, valor 78.900$")
                precio=78900
            while True:
                banco=input("Es usted cliente de bancoduoc?(escriba SI o NO):  ").upper()
                if banco=="SI":
                    preciofinal=0
                    descuento=precio*0.15
                    preciofinal=precio-descuento
                    break
                elif banco=="NO":
                    preciofinal=0
                    preciofinal=precio
                    break
            print(f"El precio final es de {preciofinal}")
                
        else:
            print("opcion fuera de rango")
    elif op==3:
        rut=input("ingrese su rut sin comas ni guion: ")
        while True:
            print("seleccione el asiento que desea eliminar")
            try:
                select=int(input(""))
                break
            except:
                print("Ingrese un numero")
        
        if 43>select and select>=1:
            selstr=str(select)
            for m in range(7):
                for n in range(6):
                    if ruts[m][n]==rut:
                        asientos[m][n]=selstr
                        nombres[m][n]=" "
                        ruts[m][n]=" "
                        telefonos[m][n]=" "
    elif op==4:
        rut=input("ingrese su rut sin comas ni guion: ")
#rut identificará la posicion
        while True:
            print("seleccione su asiento")
            try:
                select=int(input(""))
                break
            except:
                print("Ingrese un numero")
        # se valida que el asiento este dentro del rango
        if 43>select and select>=1:
            # se transforma el int a str para poder insertarlo en el arreglo
            selstr=str(select)
            # se crea el ciclo for, que recorrera la lista para encontrar en que posicion coincide el rut ingresado
            for m in range(7):
                for n in range(6):
                    if ruts[m][n]==rut:
                        print('''
1)Editar nombre
2)Editar RUT
3)Editar telefono''')
                        while True:
                            try:
                                opcion=int(input("Ingrese su opcion: "))
                            
                            except:
                                print("la opcion debe ser numerica")
                            if opcion==1 or opcion==2 or opcion==3:
                                if opcion==1:
                                    nuevonomb=input(" Ingrese el nuevo nombre")
                                    nombres[m][n]=nuevonomb
                                    break
                                if opcion==2:
                                    nuevorut=input("ingrese el nuevo rut: ")
                                    ruts[m][n]=nuevorut
                                    break
                                if opcion==3:
                                    nuevotelefon=input("ingrese el nuevo telefono: ")
                                    telefonos[m][n]=nuevotelefon
                                    break
                            else:
                                print(" Opcion fuera de rango")
print("Ha salido del sistema")


