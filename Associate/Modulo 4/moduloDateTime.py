from datetime import date as dt
import time
"""
Registro de eventos - gracias al conocimiento de la fecha y la hora, podemos determinar cuándo ocurre exactamente un error crítico en nuestra aplicación. Al crear registros, puedes especificar el formato de fecha y hora.

Seguimiento de cambios en la base de datos - a veces es necesario almacenar información sobre cuándo se creó o modificó un registro. El módulo datetime será perfecto para este caso.

Validación de datos - pronto aprenderás a leer la fecha y hora actuales en Python. Conociendo la fecha y hora actuales, podrás validar varios tipos de datos, por ejemplo, si un cupón de descuento ingresado por un usuario en nuestra aplicación sigue siendo válido.

Almacenamiento de información importante - ¿te imaginas las transferencias bancarias sin almacenar la información de cuándo se realizaron? La fecha y la hora de ciertas acciones deben conservarse y debemos ocuparnos de ello.
"""

# Obtener la fecha y hora local

today = dt.today()

print("Hoy:", today)
print("Año:", today.year)
print("Mes:", today.month)
print("Día:", today.day)

"""
Parámetro	Restricciones
year	El parámetro year debe ser mayor o igual a 1 (constante MINYEAR) y menor o igual a 9999 (constante MAXYEAR).
month	El parámetro month debe ser mayor o igual a 1 y menor o igual a 12.
day	El parámetro day debe ser mayor o igual a 1 y menor o igual que el último día del mes y año indicados.
"""
timestamp = time.time()
print("Marca de tiempo:", timestamp)

d = dt.fromtimestamp(timestamp)
print("Fecha:", d)
    
"""
A veces, es posible que debas reemplazar el año, el mes o el día con un valor diferente. No puedes hacer esto con los atributos de 
año, mes y día porque son de solo lectura. En este caso, puedes utilizar el método llamado replace
"""
d = dt(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)

class Student:
    def take_nap(self, seconds):
        print("Estoy muy cansado. Tengo que tomar una siesta. Hasta luego.")
        time.sleep(seconds) # La funcion da una respuesta un poco tarde
        print("¡Dormí bien! ¡Me siento genial!")

student = Student()
student.take_nap(5)

# Obtenemos la hora actual
hora= time.ctime()
print(hora)

"""
time.struct_time:
    tm_year   # Especifica el año.
    tm_mon    # Especifica el mes (valor de 1 a 12)
    tm_mday   # Especifica el día del mes (value from 1 to 31)
    tm_hour   # Especifica la hora (valor de 0 a 23)
    tm_min    # Especifica el minuto (valor de 0 a 59)
    tm_sec    # Especifica el segundo (valor de 0 a 61)
    tm_wday    # Especifica el día de la semana (valor de 0 a 6)
    tm_yday   # Especifica el día del año (valor de 1 a 366)
    tm_isdst  # Especifica si se aplica el horario de verano (1: sí, 0: no, -1: no se sabe)
    tm_zone   # Especifica el nombre de la zona horaria (valor en forma abreviada)
    tm_gmtoff # Especifica el desplazamiento al este del UTC (valor en segundos)
"""

"""
Creando objetos datetime

Parámetro	Restricciones
year	El parámetro year debe ser mayor o igual a 1 (constante MINYEAR) y menor o igual a 9999 (constante MAXYEAR).
month	El parámetro month debe ser mayor o igual a 1 y menor o igual a 12.
day	El parámetro day debe ser mayor o igual a 1 y menor o igual al último día del mes y año indicados.
hour	El parámetro hour debe ser mayor o igual que 0 y menor que 23.
minute	El parámetro minute debe ser mayor o igual que 0 y menor que 59.
second	El parámetro second debe ser mayor o igual que 0 y menor que 59.
microsecond	El parámetro microsecond debe ser mayor o igual que 0 y menor que 1000000.
tzinfo	El parámetro tzinfo debe ser una subclase del objeto tzinfo o None (de manera predeterminada).
fold	El parámetro fold debe ser 0 o 1 (predeterminadamente 0).
"""

