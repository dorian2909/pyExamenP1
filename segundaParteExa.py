class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad


class Editorial:
    def __init__(self, nombre, ubicacion, website):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.website = website


class Libro:
    def __init__(self, titulo, autor, editorial, fecha_publicacion, descripcion):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.fecha_publicacion = fecha_publicacion
        self.descripcion = descripcion



class Usuario:
    def __init__(self, identificacion, nombre, tipo):
        self.identificacion = identificacion
        self.nombre = nombre
        self.tipo = tipo
        self.libro_actual = None
        self.lista_libros = {}
        self.anotaciones = []

    def solicitar_prestamo(self, libro):
        if self.libro_actual is None:
            self.libro_actual = libro
            print(f"El libro '{libro.titulo}' ha sido prestado a '{self.nombre}'.")
        else:
            print(f"'{self.nombre}' ya tiene un libro prestado.")

    def agregar_a_lista(self, libro, tema):
        if tema not in self.lista_libros:
            self.lista_libros[tema] = []
            self.lista_libros[tema].append(libro)
            print(f"'{libro.titulo}' ha sido agregado a la lista de '{self.nombre}'.")

    def agregar_anotacion(self, libro, anotacion):
        for libro_anotado in self.anotaciones:
            if libro_anotado["libro"].titulo == libro.titulo:
                libro_anotado["anotaciones"].append(anotacion)
                break
        else:
            self.anotaciones.append({
                "libro": libro,
                "anotaciones": [anotacion]
            })
    def ver_anotaciones(self, libro):
        if libro in self.lista_libros:
            if "anotaciones" in self.lista_libros[libro]:
                print(f"Anotaciones para '{libro.titulo}':")
                for anotacion in self.lista_libros[libro]["anotaciones"]:
                    print(f" - {anotacion}")
            else:
                print(f"No hay anotaciones para '{libro.titulo}'.")
        else:
            print(f"'{self.nombre}' no tiene acceso al libro '{libro.titulo}'.")

    def listar_libros_prestados(self):
        return self.libros_prestados

class CreateLib:

    def __init__(self):
      self.libros = []

    def agregar_libros(self):
        # Agregando 5 libros

        libro1 =Libro(
            "El poder del ahora",
            Autor("Eckhart Tolle","alemán"),
            Editorial("Gaia Ediciones","Madrid, España","https://www.gaia.com/es"),
            "noviembre/1999",
            "El poder del ahora es un libro que invita al lector a vivir en el momento presente y dejar de preocuparse por el pasado y el futuro."
        )

        libro2 =Libro (
             "1984",
            Autor("George Orwell","George Orwell"),
            Editorial("Secker & Warburg", "Londres, Inglaterra", "https://www.penguinrandomhouse.com/books/100080/1984-by-george-orwell/"),
             "junio/1949",
             "1984 es una novela distópica que presenta una sociedad controlada por un gobierno autoritario y opresivo."
        )

        libro3 = Libro(
            "Cien años de soledad",
             Autor("Gabriel García Márquez", "colombiano"),
             Editorial("Editorial Sudamericana", "Buenos Aires, Argentina","https://www.penguinrandomhouse.com/books/404107/cien-anos-de-soledad-by-gabriel-garcia-marquez/"),
             "mayo/1967",
             "Cien años de soledad es una novela que cuenta la historia de la familia Buendía a lo largo de varias generaciones en el pueblo ficticio de Macondo."
        )

        libro4 = Libro(
            "La Odisea",
            Autor("Homero","griego"),
            Editorial("Alianza Editorial","Madrid, España","https://www.alianzaeditorial.es/libro.php?id=2489867&id_col=100500&id_subcol=100501"),
            "siglo VIII a.C.",
            "La Odisea es un poema épico que cuenta el regreso de Odiseo a casa después de la Guerra de Troya."
        )

        libro5 = Libro(
            "El Principito",
            Autor("Antoine de Saint-Exupéry","francés"),
            Editorial("Gallimard","París, Francia","https://www.gallimard.fr/Catalogue/GALLIMARD/Folio"),
            "abril/1943",
            "El Principito es un cuento filosófico que cuenta la historia de un pequeño príncipe que viaja por diferentes planetas y aprende lecciones valiosas sobre la vida y el amor."
        )
        self.libros.append(libro1)
        self.libros.append(libro2)
        self.libros.append(libro3)
        self.libros.append(libro4)
        self.libros.append(libro5)

        usuario1 = Usuario("123", "Morticia Addams", "estudiante")
        usuario2 = Usuario("456", "Tio Cosa", "profesor")

        usuario1.solicitar_prestamo(libro1)
        usuario2.solicitar_prestamo(libro2)
        usuario1.agregar_a_lista(libro1, "clásicos")
        usuario2.agregar_a_lista(libro2, "clásicos")

        usuario1.agregar_anotacion(libro1, "Me encantó este libro.")
        usuario1.ver_anotaciones(libro1)



biblioteca = CreateLib()

biblioteca.agregar_libros()




