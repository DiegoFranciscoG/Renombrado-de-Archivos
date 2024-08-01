import os
import argparse

def parsear_argumentos():
    parser = argparse.ArgumentParser(description='Renombra múltiples archivos en un directorio.')
    parser.add_argument('directorio', type=str, help='Ruta del directorio donde se encuentran los archivos.')
    parser.add_argument('--agregar_prefijo', type=str, help='Prefijo a añadir a los archivos.', default='')
    parser.add_argument('--agregar_sufijo', type=str, help='Sufijo a añadir a los archivos.', default='')
    parser.add_argument('--con_numeracion', action='store_true', help='Añade numeración a los archivos.')
    
    return parser.parse_args()

def cambiar_nombres(directorio, agregar_prefijo, agregar_sufijo, con_numeracion):
    try:
        lista_archivos = os.listdir(directorio)
        numero = 1
        
        for item in lista_archivos:
            ruta_absoluta = os.path.join(directorio, item)
            
            if os.path.isfile(ruta_absoluta):
                base, ext = os.path.splitext(item)
                
                nuevo_nombre = f"{agregar_prefijo}{base}{agregar_sufijo}{ext}"
                
                if con_numeracion:
                    nuevo_nombre = f"{agregar_prefijo}{numero}_{base}{agregar_sufijo}{ext}"
                    numero += 1
                
                nuevo_ruta = os.path.join(directorio, nuevo_nombre)
                os.rename(ruta_absoluta, nuevo_ruta)
                print(f"Renombrado: {item} -> {nuevo_nombre}")
                
    except Exception as e:
        print(f"Error al renombrar archivos: {e}")

if __name__ == "__main__":
    argumentos = parsear_argumentos()
    cambiar_nombres(argumentos.directorio, argumentos.agregar_prefijo, argumentos.agregar_sufijo, argumentos.con_numeracion)
