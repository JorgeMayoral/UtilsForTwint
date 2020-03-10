import twint
import os
import glob
import pandas
import shutil
import threading

def partirLista(lista, numero):
    numero = len(lista) // numero
    for k in range(0, len(lista), numero):
        yield lista[k:k+numero]

def busquedaTweets(lista, numero, busqueda, fecha, n):
    for usuario in lista[numero]:
        n += 1
        c = twint.Config()
        c.Search = busqueda
        c.Store_csv = True
        c.Hide_output = True
        c.Output = str(numero) + '-' + str(n) + '.csv'
        c.Since = fecha
        c.Username = usuario

        print(f'Buscando tweets mencionando "{busqueda}" de {usuario}.')

        twint.run.Search(c)

def multiusers(archivoUsuarios, busqueda, fecha, directorioSalida):
    archivo = open(archivoUsuarios, 'r')
    lineas = archivo.readlines()
    usuarios = []
    n = 0

    hilos = []
    nHilos = 5

    for i in lineas:
        usuarios.append(i.rstrip())

    if os.path.exists(directorioSalida):
        shutil.rmtree(directorioSalida)

    os.mkdir(directorioSalida)
    os.chdir(directorioSalida)

    print(f'Iniciando busqueda de "{busqueda}" de los usuarios listados en {archivoUsuarios} desde {fecha}.')

    listasUsuarios = list(partirLista(usuarios, nHilos))

    for p in range(nHilos):
        hilo = threading.Thread(target=busquedaTweets, args=(listasUsuarios, p, busqueda, fecha, n))
        hilos.append(hilo)

    for h in hilos:
        h.start()

    for h in hilos:
        h.join()

    extension = 'csv'
    archivos = [j for j in glob.glob('*.{}'.format(extension))]

    csvCombinado = pandas.concat([pandas.read_csv(f) for f in archivos])
    csvCombinado.to_csv(directorioSalida + '.csv', index=False, encoding='utf-8-sig')

    print('Busqueda terminada.')
