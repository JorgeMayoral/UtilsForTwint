import re

email_regex = (r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
delimitadorArchivo = ','

def validarEmail(strEmail):
    if re.match(email_regex, strEmail):
        return True
    return False

def escribirArchivo(listaDatos, nombreSalida):
    archivo = open(nombreSalida + '.txt', 'w+')
    strDatos = ''
    for i in listaDatos:
        strDatos = strDatos + i + '\n'
    archivo.write(strDatos)

def correo(ruta, nombreSalida):
    listaEmail = []
    archivo = open(ruta, 'r')
    listaLineas = archivo.readlines()

    for linea in listaLineas:
        i = str(linea)
        for delimitador in delimitadorArchivo:
            i = i.replace(str(delimitador), ' ')

        listaPalabras = i.split()
        for palabra in listaPalabras:
            if(validarEmail(palabra)):
                listaEmail.append(palabra)

    if listaEmail:
        uniqEmail = set(listaEmail)
        print(len(uniqEmail)," emails recolectados.")
        escribirArchivo(uniqEmail, nombreSalida)
    else:
        print('No se han encontrado emails.')