def coincidencias(archivo1, archivo2, nombreSalida):
    cuenta = 0

    archivoA = open(archivo1, 'r')
    archivoR = open(nombreSalida + '.txt', 'w')

    for lineaA in archivoA:
        archivoB = open(archivo2, 'r')
        for lineaB in archivoB:
            if lineaA == lineaB:
                if not (lineaB == 'username'):
                    cuenta +=  1
                    archivoR.write(lineaB)
        archivoB.close()

    print(f"Se han encontrado {cuenta} coincidencias.")
    print("Coincidencias almacenadas en resultado.txt")

    archivoA.close()
    archivoR.close()