from os import system

fichas = []

menu = 1

#FUNCIONES DEL PROGRAMA

def user_option():
    while True:
        try:
            userOption = int(input("1.Grabar\n2.Buscar\n3.Imprimir certificados\n4.Salir\nIngrese un dígito: "))
            system("cls")
            if userOption == 1:
                return userOption
            elif userOption == 2:
                return userOption
            elif userOption == 3:
                return userOption
            elif userOption == 4:
                return userOption
            else:
                print("Opción inválida.")
                continue
        except ValueError:
            print("Caracter no válido.")

#En esta función se harán las respectivas validaciones dependiendo del tipo de ingreso que se desee introducir.
def user_input(message, rnp=False, name=False, age=False):
    while True:
        try:
            userInput = input(message)
        #-----------VALIDACIÓN RNP------------------
            if rnp == True:
                userInput = userInput.upper()
                
                if userInput[4] != "-":
                    print("Formato inválido (9999-RTX).")
                    continue
                elif len(userInput) != 8:
                    print("Formato inválido (9999-RTX).")
                    continue
                
                rnp = userInput.split("-")
                txt = rnp[1]
                if txt.isalpha() == False:
                    raise ValueError
                numbers = rnp[0]
                if numbers.isdigit() == False:
                    raise ValueError
                
        #-----------VALIDACIÓN NOMBRE/APELLIDO------------------
            if name == True:
                userInput = userInput.capitalize()
                if len(userInput) < 3:
                    print("Demasiado corto.")
                    continue
                elif userInput.isalpha() == False:
                    raise ValueError
            
        #-----------VALIDACIÓN EDAD------------------
            if age == True:
                
                if userInput[0].isdigit() == False:
                    raise ValueError
                else:
                    age = int(userInput)
                    if age < 18:
                        print("Debe de ser Mayor de edad.")
                        continue
                    else:
                        userInput = f"{age} años"
            return userInput
        except ValueError:
            print("Caracter no válido.")
    
def grabar_ficha():
    print("GRABAR FICHA\n")
    rnp = user_input("Ingrese el RNP (Formato: 9999-RTX): ", rnp=True)
    #-------------SE VERIFICA QUE EL RNP NO TENGA UNA FICHA YA CREADA------------------------
    found = False
    for ficha in fichas:
        if ficha[0] == rnp:
            found = True
            print("RNP Ya posee una ficha.")
            break
    if found == True:
        return
    #---------------------------------------------------------------------------------------------
    name = user_input("Ingrese Nombre: ", name=True)
    lastName = user_input("Ingrese Apellido: ", name=True)
    age = user_input("Ingrese Edad: ", age=True)
    
    
    ficha = [rnp, name, lastName, age]
    fichas.append(ficha)
    
def buscar_ficha():
    print("BUSCAR FICHA\n")
    search = user_input("Ingrese el RNP: ", rnp=True)
    
    for ficha in fichas:
        if ficha[0] == search:
            print("Información relacionada:")
            print(f"RNP: {ficha[0]}")
            print(f"Nombre dueño: {ficha[1]}")
            print(f"Apellido dueño: {ficha[2]}")
            print(f"Edad: {ficha[3]}")
            break
    else:
        print("RNP no posee ficha.")
    
def impr_certificado():
    print("IMPRIMIR CERTIFICADO\n")
    search = user_input("Ingrese el RNP: ", rnp=True)
    
    for ficha in fichas:
        if ficha[0] == search:
            system("cls")
            print("Departamento de tránsito de la República de Honduras")
            print("CERTIFICADO REGISTRO NACIONAL DE PATENTES DE VEHÍCULOS\n")
            print(f"RNP: {ficha[0]}")
            print(f"Nombre dueño: {ficha[1]}")
            print(f"Apellido dueño: {ficha[2]}")
            print(f"Edad: {ficha[3]}")
            print("\nSe hace entrega de este certificado a la persona que lo solicitó.\n")
            print("Otorgado por el Departamento de tránsito de la República de Honduras.")
            break
    else:
        print("RNP no posee ficha.")

def salir():
    print("Gracias por usar nuestro Sistema.")
    menu = 0
""" PROGRAMA PRINCIPAL----------------------------------------------------- """

while menu == 1:
    userOption = user_option()
    
    match userOption:
        case 1:
            grabar_ficha()
            print(fichas)
        case 2:
            buscar_ficha()
        case 3:
            impr_certificado()
        case 4:
            menu= salir()