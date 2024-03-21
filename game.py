import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo","inteligencia"]

#Seleccionar dificultad
def select_difficulty():
    while True:
        difficulty = input("""Ingrese una dificultad: 1-Facil
                        2-Media
                        3-Dificil \n""").lower()
        if difficulty in ["facil","media","dificil"]:
            return difficulty
        else:
            print("Error, ingrese una dificultad valida: ")

difficulty = select_difficulty()

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de intentos permitidos
failures = 0

# Lista para almacenar las letras adivinadas
guessed_letters = []

displayed_letters = []

#Mostrar la palabra segun la dificultad
def display_word(secret_word, guessed_letters, difficulty):
    displayed_word= ""
    if difficulty == "facil" :
        for letter in secret_word :
            if letter in "aeiou" :
                displayed_word += letter
                displayed_letters.append(letter)
            elif letter in guessed_letters:
                displayed_word += letter
            else:
                displayed_word += "_"
    elif difficulty == "media":
        for i, letter in enumerate(secret_word):
            if letter in guessed_letters or letter == secret_word[0] or letter == secret_word[-1]:
                displayed_word += letter
                displayed_letters.append(letter)
            else:
                displayed_word += "_"
    elif difficulty == "dificil":
        for letter in secret_word:
            if letter in guessed_letters:
                displayed_word += letter
            else: 
                displayed_word += "_"
    return displayed_word

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")

#Mostrar la palabra parcialmente adivinada
word_displayed = display_word(secret_word, guessed_letters, difficulty)
print(f"Palabra: {word_displayed}")

while failures < 10:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()
    
    # Verificar si la letra ya ha sido adivinada
    if not letter.isalpha() or len(letter) != 1 :
        print("Error! Ingrese una letra: ")
        continue
    
    #Verifico si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    
    #Verifico si la letra ya era mostrada en caso de que la dificultad sea facil o media
    if letter in displayed_letters:
        print("La letra ya esta mostrada. Intenta con otra: ")
        continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print("¡Bien hecho! La letra está en la palabra.")
    else:
        print("Lo siento, la letra no está en la palabra.")
        failures += 1
    
    # Mostrar la palabra parcialmente adivinada
    word_displayed = display_word(secret_word, guessed_letters, difficulty)
    print(f"Palabra: {word_displayed}")
    
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"¡Oh no! Has llegado a tus {failures} fallos.")
    print(f"La palabra secreta era: {secret_word}")