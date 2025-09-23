def calculadora():  #Creacion de la funcion
    print("Calculadora Basica")
    #menu de la calculadora
    while True:  #utilizo el blucle para hacer el menu
        print("Opciones del Menu:")
        print("1- Suma")
        print("2- Resta")
        print("3- Division")
        print("4- multiplicacion")
        print("5- Salir del programa")
        opcion=int(input("Introduzca el numero de su opcion:")) #input para que seleccionen la opcion del menu
        #condicionales para crear las opciones
        if opcion == 1: #codigo de la suma
            while True: 
                Num= float(input("Introduzca el primer numero")) #float para capturar los numeros con decimales
                Num2= float(input("Introduzca el segundo numero"))
                Suma=Num+Num2
                print(f"{Num}+{Num2}={Suma}")
                continuar=input("Desea hacer otra suma? (Si) o (No)").lower() #Lower para volver la respuesta en minuscula
                if continuar == "no": #Para poder hacer mas de una operacion si es deseada 
                    break #break para ponerle fin al bucle
        elif opcion == 2: #codigo de la resta
            while True:
                Num= float(input("Introduzca el primer numero"))
                Num2= float(input("Introduzca el segundo numero"))
                Resta= Num-Num2
                print(f"{Num}-{Num2}={Resta}")
                continuar=input("Desea hacer otra resta? (Si) o (No)").lower()
                if continuar == "no":
                    break
        elif opcion == 3: #codigo de division
            while True:
                Num= float(input("Introduzca el primer numero"))
                Num2= float(input("Introduzca el segundo numero"))
                Division=Num/Num2
                print(f"{Num} / {Num2}={Division}")
                continuar=input("Desea hacer otra division? (Si) o (No)").lower()
                if continuar == "no":
                    break
        elif opcion == 4: #codigo de Multiplicacion
            while True:
                Num= float(input("Introduzca el primer numero"))
                Num2= float(input("Introduzca el segundo numero"))
                Multiplicacion=Num*Num2
                print(f"{Num}x{Num2}={Multiplicacion}")
                continuar=input("Desea hacer otra multiplicacion? (Si) o (No)").lower()
                if continuar == "no":
                    break
        if opcion == 5: #codigo para terminar el programa
            print("Fin del programa.")
            break
        else:   #Por si ponen un numero no permitido
            print("Esta opcion no esta disponible")

calculadora() #llamando la funcion para que se ejecute el programa