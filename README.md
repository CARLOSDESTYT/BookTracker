# Acerca de BookTracker
BookTracker es una plataforma diseñada para acompañar y motivar a los lectores en su camino. Permite registrar los libros que han leído, llevar un seguimiento visual de su progreso y descubrir estadísticas personalizadas que muestran cómo ha evolucionado su hábito de lectura a lo largo del tiempo.

Inspirada en la idea de un “Reading Wrapped”, BookTracker transforma la experiencia lectora en algo más dinámico y significativo. Los usuarios pueden consultar datos como sus géneros favoritos, autores más leídos, número de libros por mes, y más, todo dentro de una interfaz clara, moderna y pensada para brindar una experiencia agradable.

El objetivo de BookTracker es brindar una herramienta sencilla y funcional para los lectores que desean monitorear su hábito de lectura, visualizar sus avances diarios y mantener todos sus libros registrados en un solo lugar.

Construido con Django, Python y manejo de base de datos con SQLite, BookTracker ofrece una interfaz amigable.






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
