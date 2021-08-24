def main():
    #escribe tu código abajo de esta línea
    msj = int(input("Dame el número de mensajes: "))
    megas = float(input("Dame el número de megas: "))
    minutos = int(input("Dame el número de minutos: "))
    total = ((msj * 0.80)+ (megas * 0.80) + (minutos * 0.80))
    print("El costo mensual es:", total)

if __name__ == '__main__':
    main()
