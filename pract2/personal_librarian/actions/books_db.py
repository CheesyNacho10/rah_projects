from fuzzywuzzy import process, fuzz

class BooksDB:
  def find_books_by_genre_fuzzy(genre, threshold=80):
    results = []
    for book_id, book in BooksDB.books_db.items():
      ratio = process.extractOne(book["genre"], [genre], scorer=fuzz.token_sort_ratio)
      if ratio[1] >= threshold:
        results.append(book)
    return results

  books_db = {
    "id_0": {
      "title": "El nombre del viento",
      "author": "Patrick Rothfuss",
      "genre": "fantasía"
    },
    "id_1": {
      "title": "El temor de un hombre sabio",
      "author": "Patrick Rothfuss",
      "genre": "fantasía"
    },
    "id_2": {
      "title": "El imperio final",
      "author": "Brandon Sanderson",
      "genre": "fantasía"
    },
    "id_3": {
      "title": "El pozo de la ascensión",
      "author": "Brandon Sanderson",
      "genre": "fantasía"
    },
    "id_4": {
      "title": "El héroe de las eras",
      "author": "Brandon Sanderson",
      "genre": "fantasía"
    },
    "id_5": {
      "title": "Elantris",
      "author": "Brandon Sanderson",
      "genre": "fantasía"
    },
    "id_6": {
      "title": "La guerra de los cielos",
      "author": "Fernando Trujillo",
      "genre": "fantasía"
    },
    "id_7": {
      "title": "La marca del guerrero",
      "author": "Fernando Trujillo",
      "genre": "fantasía"
    },
    "id_8": {
      "title": "La ira de los dragones",
      "author": "Fernando Trujillo",
      "genre": "fantasía"
    },
    "id_9": {
      "title": "La maldición del maestro",
      "author": "Fernando Trujillo",
      "genre": "fantasía"
    },
    "id_10": {
      "title": "El código Da Vinci",
      "author": "Dan Brown",
      "genre": "misterio"
    },
    "id_11": {
      "title": "Ángeles y demonios",
      "author": "Dan Brown",
      "genre": "misterio"
    },
    "id_12": {
      "title": "El símbolo perdido",
      "author": "Dan Brown",
      "genre": "misterio"
    },
    "id_13": {
      "title": "Inferno",
      "author": "Dan Brown",
      "genre": "misterio"
    },
    "id_14": {
      "title": "Origen",
      "author": "Dan Brown",
      "genre": "misterio"
    },
    "id_15": {
        "title": "Cien años de soledad",
        "author": "Gabriel García Márquez",
        "genre": "realismo mágico"
    },
    "id_16": {
        "title": "Crónica de una muerte anunciada",
        "author": "Gabriel García Márquez",
        "genre": "realismo mágico"
    },
    "id_17": {
        "title": "1984",
        "author": "George Orwell",
        "genre": "distopía"
    },
    "id_18": {
        "title": "Rebelión en la granja",
        "author": "George Orwell",
        "genre": "distopía"
    },
    "id_19": {
        "title": "Fahrenheit 451",
        "author": "Ray Bradbury",
        "genre": "distopía"
    },
    "id_20": {
        "title": "Orgullo y prejuicio",
        "author": "Jane Austen",
        "genre": "romance"
    },
    "id_21": {
        "title": "Jane Eyre",
        "author": "Charlotte Brontë",
        "genre": "romance"
    },
    "id_22": {
        "title": "La chica del tren",
        "author": "Paula Hawkins",
        "genre": "thriller"
    },
    "id_23": {
        "title": "Gone Girl",
        "author": "Gillian Flynn",
        "genre": "thriller"
    },
    "id_24": {
        "title": "El psicoanalista",
        "author": "John Katzenbach",
        "genre": "thriller"
    },
    "id_25": {
        "title": "Sapiens: De animales a dioses",
        "author": "Yuval Noah Harari",
        "genre": "no ficción"
    },
    "id_26": {
        "title": "Homo Deus: Breve historia del mañana",
        "author": "Yuval Noah Harari",
        "genre": "no ficción"
    },
    "id_27": {
        "title": "Cosmos",
        "author": "Carl Sagan",
        "genre": "ciencia"
    },
    "id_28": {
        "title": "Una breve historia del tiempo",
        "author": "Stephen Hawking",
        "genre": "ciencia"
    },
     "id_29": {
        "title": "Los pilares de la Tierra",
        "author": "Ken Follett",
        "genre": "histórica"
    },
    "id_30": {
        "title": "Un mundo sin fin",
        "author": "Ken Follett",
        "genre": "histórica"
    },
    "id_31": {
        "title": "La sombra del viento",
        "author": "Carlos Ruiz Zafón",
        "genre": "misterio"
    },
    "id_32": {
        "title": "El juego del ángel",
        "author": "Carlos Ruiz Zafón",
        "genre": "misterio"
    },
    "id_33": {
        "title": "El prisionero del cielo",
        "author": "Carlos Ruiz Zafón",
        "genre": "misterio"
    },
    "id_34": {
        "title": "El laberinto de los espíritus",
        "author": "Carlos Ruiz Zafón",
        "genre": "misterio"
    },
    "id_35": {
        "title": "Tokio Blues",
        "author": "Haruki Murakami",
        "genre": "contemporánea"
    },
    "id_36": {
        "title": "1Q84",
        "author": "Haruki Murakami",
        "genre": "contemporánea"
    },
    "id_37": {
        "title": "Kafka en la orilla",
        "author": "Haruki Murakami",
        "genre": "contemporánea"
    },
    "id_38": {
        "title": "La chica que soñaba con una cerilla y un bidón de gasolina",
        "author": "Stieg Larsson",
        "genre": "thriller"
    },
    "id_39": {
        "title": "Los hombres que no amaban a las mujeres",
        "author": "Stieg Larsson",
        "genre": "thriller"
    },
    "id_40": {
        "title": "La reina en el palacio de las corrientes de aire",
        "author": "Stieg Larsson",
        "genre": "thriller"
    }
  }
