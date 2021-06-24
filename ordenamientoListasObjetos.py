
class Persona:
    def __init__(self,nombre,edad,dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

class Alumno(Persona):
    def __init__(self,nombre,edad,dni,codigo,nota):
        super().__init__(nombre,edad,dni)
        self.nota = nota
        self.codigo = codigo


listaALumno=[]
class clase_UP:
    def __init__(self,listaALumno):
        self.listaALumno = listaALumno

    def ingresar_alumno(self,alumno):
        self.listaALumno.append(alumno)

    def mostrar_alumno(self):
        for alumno in self.listaALumno:
            print(alumno.nombre,str(alumno.edad),str(alumno.dni),alumno.codigo,str(alumno.nota))


    def ordenar_por_edad(self):
        lista=sorted(self.listaALumno,key=lambda objeto:objeto.edad)
        for x in lista:
            print(x.nombre, str(x.edad), str(x.dni), x.codigo, str(x.nota))



    def ordenar_por_nota(self):
        lista = sorted(self.listaALumno, key=lambda objeto: objeto.nota,reverse=False)
        for x in lista:
             print(x.nombre, str(x.edad), str(x.dni), x.codigo, str(x.nota))

    def cuadro_de_Merito(self):
        lista = sorted(self.listaALumno, key=lambda objeto: objeto.nota,reverse=True)
        for x in lista:
             print(x.nombre, str(x.edad), str(x.dni), x.codigo, str(x.nota))



alumno1=Alumno("karla",18,410021,"000021",17)
alumno2=Alumno("jonas",19,421222,"000032",13)
alumno3=Alumno("karina",21,430909,"000056",19)
alumno4=Alumno("pepe",17,418787,"000078",12)
alumno5=Alumno("armando",22,458989,"000091",18)

listaAlumnos1=[]
objlista1=clase_UP(listaAlumnos1)

objlista1.ingresar_alumno(alumno1)
objlista1.ingresar_alumno(alumno2)
objlista1.ingresar_alumno(alumno3)
objlista1.ingresar_alumno(alumno4)
objlista1.ingresar_alumno(alumno5)

objlista1.mostrar_alumno()
print()
print("ordenar por edad")
objlista1.ordenar_por_edad()
print()
print("ordenar por nota")
objlista1.ordenar_por_nota()
print()
print("Cuadro de merito")
objlista1.cuadro_de_Merito()


