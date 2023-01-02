text = input("Introduce un texto para convertirlo a lenguaje hacker: ")

def leet(text):
    # Creamos una tabla de correspondencias
    leet_chars = {
        'a': '4',
        'b': 'l3',
        'c': '(',
        'd': '[)',
        'e': '3',
        'f': '|=',
        'g': '6',
        'h': '|-|',
        'i': '1',
        'j': '_|',
        'k': '|<',
        'l': '|_',
        'm': '|\\/|',
        'n': '|\\|',
        'o': '0',
        'p': '|*',
        'q': '(_,)',
        'r': '|2',
        's': '5',
        't': '7',
        'u': '|_|',
        'v': '\\/',
        'w': '\\/\\/',
        'x': '><',
        'y': '`/',
        'z': '2'

    }

    # Creamos una cadena vacía para almacenar el texto en "leet"
    leet_text = ""

    # Iteramos sobre cada carácter del texto original
    for char in text:
        # Si el carácter está en nuestra tabla de correspondencias, lo sustituimos
        if char.lower() in leet_chars:
            leet_text += leet_chars[char.lower()]
        # Si no, lo agregamos tal cual al texto en "leet"
        else:
            leet_text += char

    # Devolvemos el texto en "leet"
    return leet_text

# Imprimimos leet_text
print(leet(text))
