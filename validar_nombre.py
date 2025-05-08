# Validar nombre al usuario
def validar_nombre():
    nombre = input("Ingrese su nombre y apellido por favor:\n").strip()
    if len(nombre.split()) >= 2 and nombre.istitle():
        return "Nombre valido"
    else:
        return "Nombre invalido"
    
print(validar_nombre())

