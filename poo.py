#Herencias
#Persona-Nombre, Edad, genero
#Trabajador - Salario, Horario
#Estudiante - Calificaciones, Cantidad Materias

class Persona:
    def __init__(self,nombre, edad, genero, curp):
        self._nombre = nombre
        self._edad = edad
        self._genero = genero
        self.__curp = curp
    
    def identificacion(self):
        return f"La persona {self._nombre} tiene {self._edad} de edad y su genero es {self._genero}"
    
    def mostrar_curp(self):
        return f"La curp de la persona es: {self.__curp}"

class Trabajador(Persona):
    def __init__ (self,nombre,edad,genero,curp,empresa,salario,puesto):
        super().__init__(nombre,edad,genero,curp)
        self.__salario=salario
        self._puesto=puesto
        self.empresa=empresa

    def accion(self):
        return f"Actualmente trabaja en {self.empresa} y gana {self.__salario} a la semana con su puesto de {self._puesto}"
    
    def aumento(self,monto):
        self.__salario+=monto
        print (f"La persona {self._nombre} ha recibido un aumento, su salario actual es de {self.__salario}")

class Estudiante(Persona):
    def __init__(self,nombre,edad,genero,curp,calificacion,canMaterias,grado,nom_escuela):
        super().__init__(nombre,edad,genero,curp)
        self.__calificacion=calificacion
        self._canMaterias=canMaterias
        self._grado=grado
        self.nom_escuela=nom_escuela

    def accion(self):
        return f"Actualmente estudia el {self._grado} grado en {self.nom_escuela} y lleva {self._canMaterias} materias con promedio de {self.__calificacion}"
    
    def calificacion_final(self,calificacion):
        self.__calificacion=(self.__calificacion+calificacion)/2
        print (f"La calificacion final de {self._nombre} es de: {self.__calificacion}")

trabajador1=Trabajador('Juan',26,'Masculino','JM01','Nasa',3000,'Vigilante')

estudiante1=Estudiante('Luz',14,'Femenino','LF02',10,6,3,'Insurgentes')

personas=(trabajador1,estudiante1)

print("\n")
for persona in personas:
    print(persona.identificacion())
    print(persona.accion())
    print(persona.mostrar_curp())
    print("\n")

trabajador1.aumento(100)
estudiante1.calificacion_final(9)


