import random

respuesta = "y"

while respuesta == "y":
    numeroDado = random.randint(1,6)

    if numeroDado == 1:
        print("-------")
        print("       ")
        print("   0   ") 
        print("       ")
        print("-------")
    elif numeroDado == 2:
        print("-------")
        print("       ")
        print("  0 0  ") 
        print("       ")
        print("-------")
    elif numeroDado == 3:
        print("-------")
        print("       ")
        print(" 0 0 0 ") 
        print("       ")
        print("-------")
    elif numeroDado == 4:
        print("-------")
        print(" 0   0 ")
        print("       ") 
        print(" 0   0 ")
        print("-------")
    elif numeroDado == 5:
        print("-------")
        print(" 0   0 ")
        print("   0   ") 
        print(" 0   0 ")
        print("-------")
    elif numeroDado == 6:
        print("-------")
        print(" 0   0 ")
        print(" 0   0 ") 
        print(" 0   0 ")
        print("-------")
    
    pregunta = input('¿Quieres tirar el dado? si: "y", no: "n"')
    respuesta = pregunta