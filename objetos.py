# class Empleado:
#     def __init__(self, nombre, salario):
#         self.nombre=nombre
#         self.salario=salario

#     def obtener_informacion(self):
#         return f"Nombre: {self.nombre}, Salario: ${self.salario}"
    
#     def aumentar_salario(self, porcentaje):
#         aumento = self.salario*(porcentaje/100)
#         self.salario += aumento 
#         return f"¡Aumento del {porcentaje}% aplicado! Nuevo salario: ${self.salario}"
    
#Methods: study, do homework, attend classes
class Alumno: 
    def __init__(self,nombre, id, calificacion):
        self.nombre=nombre
        self.id=id
        self.calificacion=calificacion
    
    def estudiar (self, materia):
        return f"El alumno {self.nombre} ha estudiado {materia}"
    
    def hacer_tarea (self,calificacion_tarea):
        self.calificacion=(self.calificacion+calificacion_tarea)/2
        return  f"El alumno {self.nombre} ha obtenido {calificacion_tarea} en su tarea \n y su promedio es {self.calificacion}"
    
    def asistir_clase(self, asistencia):
        if asistencia == 10:
            return "El alumno ha asistido todos los dias"
        else:
            return f"El alumno tuvo {asistencia} faltas"
        

alumno1=Alumno('Jose',1,9)
alumno2=Alumno('Roberto',2,8)

print(f"Nombre: {alumno1.nombre} ID: {alumno1.id} Calif: {alumno1.calificacion}")
print(alumno1.estudiar('Fisica'))
print(alumno1.hacer_tarea(10))
print(alumno1.asistir_clase(10))

print(f"Nombre: {alumno2.nombre} ID: {alumno2.id} Calif: {alumno2.calificacion}")
print(alumno2.estudiar('Matematicas'))
print(alumno2.hacer_tarea(9))
print(alumno2.asistir_clase(9))