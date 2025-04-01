# Solicitar información al alumno como nombre , edad ,fecha de nacimiento :
nombre = input("Por favor, ingresa tu nombre: ")
edad = input("Por favor, ingresa tu edad: ")
fecha_nac = input("Por favor, ingresa tu fecha de nacimiento (DD/MM/AAAA): ")

linea=[f"Nombre: {nombre}"+'\n',f"Edad: {edad}"+'\n',f"Fecha de nacimiento: {fecha_nac}"+'\n',]

with open('trabajo.txt','a') as comotellamas:
    comotellamas.writelines(linea)

with open('trabajo.txt','r') as texto:
    info=texto.read()
    print(info)


