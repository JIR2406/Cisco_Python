import os

directorio = "C:/Users/jairg/Downloads/Fotos Miercoles 12 de Julio"  # Ruta del directorio a examinar
cod=1
archivos = os.listdir(directorio)


for nombre_archivo in archivos:
    
    if not nombre_archivo.startswith("00"):
            nuevo_nombre = "0" + str(cod)+".jpg"
            cod+=1
            ruta_original = os.path.join(directorio, nombre_archivo)
            ruta_nuevo_nombre = os.path.join(directorio, nuevo_nombre)
            os.rename(ruta_original, ruta_nuevo_nombre)
            print(f"Se registro el archivo: {nuevo_nombre}")
    elif not nombre_archivo.startswith("0"):
            nuevo_nombre = "0" + str(cod)+".jpg"
            cod+=1
            ruta_original = os.path.join(directorio, nombre_archivo)
            ruta_nuevo_nombre = os.path.join(directorio, nuevo_nombre)
            os.rename(ruta_original, ruta_nuevo_nombre)
            print(f"Se registro el archivo: {nuevo_nombre}")