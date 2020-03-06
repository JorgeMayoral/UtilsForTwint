import argparse

import tabla
import correo
import coincidencias

parser = argparse.ArgumentParser(description='Procesa datos (en archivos .csv) obtenidos con Twint.')

parser.add_argument('-t', '--tabla', action='store',
    help='Crea una tabla con los datos del archivo CSV. Por defecto simplificada, usa -f para mostrarla completa')

parser.add_argument('-f', '--full', action='store_true',
    help='La tabla generada muestra todos los datos recogidos por Twint.')

parser.add_argument('-e', '--email', action='store',
    help='Extrae los emails de una serie de tweets.')

parser.add_argument('-c', '--coincidencias', nargs=2, action='store',
    help='Extrae las coincidencias entre 2 listas de seguidores o seguidos.')

parser.add_argument('-o', '--output', action='store',
    help='Especifica el nombre del archivo de salida (sin extensión).')

args = parser.parse_args()

nombreSalida = 'resultado'

if args.output != None:
    nombreSalida = args.output

if args.tabla != None:
    tabla.tabla(args.tabla, nombreSalida, args.full)

if args.email != None:
    correo.correo(args.email, nombreSalida)

if args.coincidencias != None:
    archivo1 = args.coincidencias[0]
    archivo2 = args.coincidencias[1]

    coincidencias.coincidencias(archivo1, archivo2, nombreSalida)
