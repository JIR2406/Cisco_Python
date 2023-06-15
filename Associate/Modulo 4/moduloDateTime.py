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
    