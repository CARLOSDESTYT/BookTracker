while True:
    paginas_totales = input("Ingresa la cantidad de páginas totales del libro:  ")
    if int(paginas_totales) == 0:
        break
    paginas_leídas = input("Ingresa la cantidad de páginas leídas:  ")
    paginas = int(paginas_totales) - int(paginas_leídas)

    for dia in range(1, 11):
        x_dia = int(paginas)/dia
        print(f"{dia} páginas por día -> {x_dia}")
