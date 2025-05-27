# Solicitar información al alumno como nombre , edad ,fecha de nacimiento :
class Alumnos:
    def escritura_de_alumnos(self):
        nombre = input("Por favor, ingresa tu nombre: ")
        edad = input("Por favor, ingresa tu edad: ")
        fecha_nac = input("Por favor, ingresa tu fecha de nacimiento (DD/MM/AAAA): ")

        linea=[f"Nombre: {nombre}"+'\n',f"Edad: {edad}"+'\n',f"Fecha de nacimiento: {fecha_nac}"+'\n',]

        with open('trabajo.txt','a') as comotellamas:
            comotellamas.writelines(linea)

    def lectura_de_alumnos(self):
        with open('trabajo.txt','r') as texto:
            info=texto.read()
            print(info)

alumnos = Alumnos()
alumnos.escritura_de_alumnos()
alumnos.lectura_de_alumnos()
