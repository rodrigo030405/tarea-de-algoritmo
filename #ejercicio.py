#ejercicio 
import numpy
import os
import time
import msvcrt
arreglo_restaurant=numpy.zeros((3,3),int)
lista_ruts=[]
lista_nombres=[]
lista_correos=[]
lista_filas=[]
lista_columnas=[]
lista_cant_personas=[]
lista_comida=[]
lista_postre=[]
lista_bebida=[]
os.system('cls')
while True:
    print(""" menu restaurant
    1. ver mesas disponibles
    2. reserva mesas
    3. carta
    4. pagar 
    5. cancelar
    6. salir""")  
    while True:
        try:
            opcion=int(input("ingrese opcion: "))
            if opcion in(1,2,3,4,5,6):
                break
            else:
                print("error, opcion incorrecta")
        except:
            print("error, debe ingresa un numero entero")
    os.system('cls')
    if opcion==1:
        
        for x in range(3):
            print(f"mesas  {x+1}", end=" ")
            for y in range(3):
                print(arreglo_restaurant[x][y], end=" ")
            print()
        print("         1 2 3 ")    
        print("        columna")
        print("\n presione una tecla para continuar...")
        msvcrt.getch()
        os.system('cls')
    elif opcion==2:  
        if 0 not in arreglo_restaurant:
            print("el restaurante esta lleno")
            time.sleep(3)
            continue
        print("reserva de mesa")
        while True:
            try:
                rut=int(input("ingrese su rut (sin puntos ni digito verificador): "))
                if rut >=1000000 and rut<=99999999:
                    break
                else:
                    print("error el debe estar entre 1000000 y 99999999")
                    time.sleep(3)
            except:
                  print("error debe ingresar un numero entero")
                  time.sleep(3)
        if rut in lista_ruts:
            print("cliente ya registrado, no puede comprar otra entrada")
            time.sleep(3)
            continue                   
        while True:
            nombre=(input("ingrese su nombre: "))
            if len(nombre.strip())>=3 and nombre.isalpha():
                break
            else:
                print("error el nombre debe tener al menos 3 letras")
                time.sleep(3)
                os.system('cls')
        while True:
            correo=(input("ingrese su correo: "))
            if "@" in correo:
                break
            else:
                print(" error formato de correo incorrecto")
                time.sleep(3)
               
        while True:
            try:
                cant_personas=int(input("cuantas personas son en total"))
                if cant_personas<=6 and cant_personas>=1:
                    break
                else:
                    print("demasiadas personas, NO HAY MESAS CON ESE CUPO")
                    time.sleep(3)
                    
            except:
                print("error, ingrese un numero positivo")        
        lista_ruts.append(rut)
        lista_nombres.append(nombre)
        lista_correos.append(correo)
        lista_cant_personas.append(cant_personas)
        print("cliente registrado con exito")
        time.sleep(3)                    
        while True:
            try:
                fila=int(input(" ingrese numero de fila(1-3): "))
                columna=int(input("ingrese numero de columna(1-3)"))
                if fila<=3 and fila>=1 and columna<=3 and columna>=1:
                    if arreglo_restaurant[fila-1][columna-1]==0:       
                        arreglo_restaurant[fila-1][columna-1]=1
                        lista_filas.append(fila)
                        lista_columnas.append(columna)
                        print("mesa comprado con exito")
                        time.sleep(3)
                        
                        break
                    else:
                        print("mesa ocupada, lo siento")
                        time.sleep(3)
                        
                else:
                    print("error, ingrese el numero de una mesa disponible")
                    time.sleep(3)
                    
            except:
                print("error ingrese un numero entero")
                time.sleep(3)              
    elif opcion==3:
        while True:
            try :
                print(""" menu de comida
                1. bebidas
                2. platos
                3. postre
                4. pedir
                5. cancelar""")
                eleccion=int(input("elija que dea comer"))
                if eleccion in(1,2,3,4,5):
                    break
                else:
                    print("elija una opcion valida")
                    os.system('cls')
            except:
                print("error coloque un numero entero")
                os.system('cls')
        if eleccion==1:
            print(f"""
            """)
            pass
        elif eleccion==2:
            print(f"")
            pass
        elif eleccion==3:
            print(f"")
            pass
        elif eleccion==4:
            print()
            pass
        elif eleccion==5:
            print("")
            pass

    elif opcion==4:
        pass
    elif opcion==5:
        pass
    elif opcion==6:
        break             
    