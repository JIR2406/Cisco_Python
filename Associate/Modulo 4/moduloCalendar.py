import calendar
print(calendar.calendar(2023)) #Funcion que imprime el calendario
# Se le pasa el año que necesitemos


print(calendar.month(2020, 11)) # Lo puestra por mes


from datetime import datetime
 
datetime = datetime(2019, 11, 27, 11, 27, 22)
print(datetime.strftime('%y/%B/%d %H:%M:%S'))

