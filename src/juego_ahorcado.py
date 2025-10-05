import random

def elige_palabra(fichero="palabras.txt"):
    """
    Devuelve una palabra aleatoria tomada de un fichero de texto.

    Parámetros:
        fichero: ruta al archivo que contiene las palabras (una por línea).

    Devuelve:
        Una palabra (str) elegida al azar del fichero.
    """
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
    # Quitar saltos de línea y espacios
    palabras = [linea.strip() for linea in lineas if linea.strip() != ""]
    return random.choice(palabras)


def normalizar(cadena):
    cadena = cadena.lower().strip()
    res = ""
    for c in cadena:
        if c in "áä":
            res += "a"
        elif c in "éë":
            res += "e"
        elif c in "íï":
            res += "i"
        elif c in "óö":
            res += "o"
        elif c in "úü":
            res += "u"
        else:
            res+=c
    return res
            
    """
    Normaliza una cadena de texto realizando las siguientes operaciones:
        - convierte a minúsculas
        - quita espacios en blanco al principio y al final
        - elimina acentos y diéresis        
    
    Parámetros:
      cadena: cadena de texto que hay que sanear
    
    Devuelve:
      Cadena de texto con la palabra normalizada
    """

def ocultar(palabra_secreta, letras_usadas=""):
    res=""
    for letra in palabra_secreta:
        if letra in letras_usadas:
            res += letra
        else:
            res += "_"
    return res
    '''Devuelve una cadena de texto con la palabra enmascarada. 
    Las letras que no están en letras_usadas se muestran como guiones bajos (_).

    Parámetros:
    - palabra_secreta: cadena de texto con la palabra que se debe enmascarar
    - letras_usadas: cadena de texto con las letras que se deben mostrar (por defecto cadena vacía)

    Devuelve:
      Cadena de texto con la palabra enmascarada
    '''
    


def ha_ganado(palabra_enmascarada):
    if "_" not in palabra_enmascarada:
        return True
    else:
        return False
    '''Devuelve True si el jugador ha ganado (es decir, si no quedan letras por descubrir en la palabra enmascarada).

    Parámetros:
    - palabra_enmascarada: cadena de texto con la palabra enmascarada 

    Devuelve:
    - True si el jugador ha ganado, False en caso contrario
    '''



def mostrar_estado(palabra_enmascarada, letras_usadas, intentos_restantes = 6):
    print(f"Estado: {"".join(palabra_enmascarada)}")
    if letras_usadas == "":
        print(f"Letras usadas: Ninguna")
    else:
        print(f"Letras usadas: {letras_usadas}")
    print(f"Intentos restantes:{intentos_restantes}")


def pedir_letra(letras_usadas):
    letra = input("Introduce una letra:")
    while True:
        if len(letra) != 1:
            print("Introduzca una única letra")
            letra = input("Introduce una letra:")
        elif letra in letras_usadas:
            print("Esa letra ya la has usado anteriormente")
            letra = input("Introduce una letra:")
        else:
            return letra.lower() 
        


def jugar(palabra_secreta, intentos_restantes):
    palabra_secreta = normalizar(palabra_secreta)
    if palabra_secreta == "":
        return None
    palabra_enmascarada = ocultar(palabra_secreta)
    letras_usadas = ""
    while intentos_restantes > 0 and "_" in palabra_enmascarada:
        mostrar_estado(palabra_enmascarada, letras_usadas, intentos_restantes)
        letra = pedir_letra(letras_usadas) 
        letras_usadas += letra
        if letra not in palabra_secreta:
            print(f"Has fallado")
            intentos_restantes -= 1
        elif letra in palabra_secreta:
            print(f"La letra está en la palabra secreta")
            palabra_enmascarada = ocultar(palabra_secreta, letras_usadas) 
    victoria = ha_ganado(palabra_enmascarada)
    if victoria == True:
        print("Has ganado!")
    elif victoria == False:
        print(f"Has perdido!")

        
        
        

# Programa principal

palabra_secreta = elige_palabra()
intentos_restantes = 6
jugar(palabra_secreta, intentos_restantes)