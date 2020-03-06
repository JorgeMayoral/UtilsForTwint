import pandas
import webbrowser
import csv
import os
from tabulate import tabulate

htmlStart = '''
    <!DOCTYPE html>
    <html lang="es">
        <head>
            <title>Utils For Twint</title>
            <meta charset="UTF-8">
            <style>
                table { border-collapse: collapse; width: 100%; }
                th, td { text-align: left; padding: 8px; }
                tr:nth-child(even) { background-color: #f2f2f2 }
                th { background-color: #006666; color: white; }
            </style>
        </head>
        <body>'''

htmEnd = '''
        </body>
    </html>'''

def tabla(archivo, nombreSalida, completa):
    pandatabulate = lambda df: tabulate(df, headers='keys', tablefmt='html')
    # Eliminar limite de columnas mostradas
    pandas.options.display.max_columns = None
    # Todos los datos en una sola linea
    pandas.options.display.width = None

    archivoOriginal = archivo

    if not completa:

        # Eliminar columnas no utiles del csv
        archivoModificado = 'modificado.csv'

        print('Eliminando columnas innecesarias...')


        columnasEliminables = [0,1,2,5,6,9,11,12,13,14,15,16,17,18,20,
                            21,22,23,24,25,26,27,28,29,30,31,32,33]
        columnasEliminables = sorted(columnasEliminables, reverse=True)
        cuentaFilas = 0

        with open(archivoOriginal, 'r') as fuente:
            lector = csv.reader(fuente)
            with open(archivoModificado,'w', newline='') as resulatado:
                escritor = csv.writer(resulatado)
                for fila in lector:
                    cuentaFilas += 1
                    for indiceColumnas in columnasEliminables:
                        del fila[indiceColumnas]
                    escritor.writerow(fila)

        print(f'Leyendo datos de {archivo}...')
        df = pandas.read_csv((archivoModificado), index_col = 'date')

        print('Eliminando archivos temporales...')
        os.remove(archivoModificado)

    else:
        print(f'Leyendo datos de {archivo}...')
        df = pandas.read_csv((archivoOriginal), index_col = 'date') 

    print(f'Generando {nombreSalida}.html...')
    htmlGenerado = open(nombreSalida + '.html', 'w')
    htmlGenerado.write(htmlStart)
    htmlGenerado.write(pandatabulate(df))
    htmlGenerado.write(htmEnd)
    htmlGenerado.close()
    print(f'Archivo {nombreSalida}.html generado.')

    print('Abriendo...')
    webbrowser.open(nombreSalida + '.html')
