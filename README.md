# BookTracker
libros = []

def agregar_libro():
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    paginas = int(input("Número de páginas: "))
    
    libro = {
        'titulo': titulo,
        'autor': autor,
        'paginas': paginas,
        'pagina_actual': 0,
        'completado': False
    }
    
    libros.append(libro)
    print(f" Libro '{titulo}' agregado!")

def ver_libros():
    print("\n TUS LIBROS:")
    for i, libro in enumerate(libros, 1):
        estado = " COMPLETADO" if libro['completado'] else f"📖 Página {libro['pagina_actual']}/{libro['paginas']}"
        print(f"{i}. {libro['titulo']} - {estado}")

def actualizar_progreso():
    ver_libros()
    try:
        numero = int(input("Número del libro: ")) - 1
        nueva_pagina = int(input("¿En qué página vas?: "))
        
        libros[numero]['pagina_actual'] = nueva_pagina
        
        if nueva_pagina >= libros[numero]['paginas']:
            libros[numero]['completado'] = True
            print("¡Libro completado!")
        else:
            progreso = (nueva_pagina / libros[numero]['paginas']) * 100
            print(f"Progreso: {progreso:.1f}%")
            
    except:
        print(" Error: Número inválido")

# Menú principal
while True:
    print("\n" + "="*40)
    print(" MI BIBLIOTECA PERSONAL")
    print("="*40)
    print("1. Agregar libro")
    print("2. Ver libros")
    print("3. Actualizar progreso")
    print("4. Salir")
    
    opcion = input("Elige una opción (1-4): ")
    
    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        ver_libros()
    elif opcion == "3":
        actualizar_progreso()
    elif opcion == "4":
        print("¡Hasta pronto!")
        break
    else:
        print("Opción inválida")
