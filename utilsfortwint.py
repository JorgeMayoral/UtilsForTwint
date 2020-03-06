import argparse
import email

parser = argparse.ArgumentParser(description='Procesa datos obtenidos con Twint.')

parser.add_argument('-t', '--tabla', action='store',
    help='Crea una tabla con los datos del archivo CSV.')

parser.add_argument('-e', '--email', action='store',
    help='Extrae los emails de una serie de tweets.')

parser.add_argument('-o', '--output', action='store',
    help='Especifica el nombre del archivo de salida (sin extensión).')

args = parser.parse_args()

nombreSalida = 'resultado'

if args.output != None:
    nombreSalida = args.output

if args.email != None:
    email.extraer(args.email, nombreSalida)
