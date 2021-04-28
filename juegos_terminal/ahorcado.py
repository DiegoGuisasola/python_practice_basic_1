# Author: Diego Guisasola

from os import system

cls = lambda: system("cls")  # Para limpiar la pantalla

# Class Player. Por el momento sólo consta de un atributo. Escalable a multiplayer.
class Player:
    def __init__(self, vidas=3):
        self.vidas = vidas


# Para implementar varios jugadores:
# 1. En el constructor de la clase Ahorcado() se puede agregar una variable (cantidad_jugadores: int) que pida la cantidad de jugadores.
# 2. Crear una lista de objectos de la clase Player(). El tamaño lo determina cantidad_jugadores.
# 3. Implementar un método que itere por cada jugador.
# NOTA: Si se plantea implementar algo de estas características, es recomendable primero trabajar en la GUI y luego en multijugador.

# Class Game. Controla todo el juego
class Ahorcado:
    # Constructor
    def __init__(self, palabra: str = "test"):
        self.p1 = Player()
        self.is_game_over = False
        self.palabra = palabra
        self.letras_usadas = list()
        self.mostrar_palabra = list("_" * len(palabra))

    # Obtener la letra del jugador
    def get_guess(self):
        guess = ""
        print("Ingrese una letra:", end=" ")
        while len(guess) != 1:  # Mientras sólo presionen ENTER o ingresen varias letras
            guess = input()
        return guess

    # Obtener las posiciones de las letras en caso se haya adivinado correctamente
    def get_index(self, letra):
        indices = [index for index, word in enumerate(self.palabra) if word == letra]
        return indices

    # Actualizar la palabra mostrada en pantalla
    def letter_guessed(
        self, guess
    ):  # Actualiza la lista mostrada al jugador con la palabra a adivinar oculta.
        indices = self.get_index(guess)  # Get all indices
        for i in indices:
            self.mostrar_palabra[i] = guess

    # Verificar si el jugador ganó
    def check_if_player_won(self):
        if not "_" in self.mostrar_palabra:
            self.player_won()

    # El jugador ganó. Se pueden implementar cosas adicionales en este método.
    def player_won(self):
        self.game_over()
        return

    # Game Manager
    def play(self):
        while not self.is_game_over:
            self.display()
            guess = self.get_guess()  # 1. Get guess
            if guess in self.palabra:  # Si está en la palabra
                self.letter_guessed(guess)
                self.check_if_player_won()
            else:  # Si NO esta en la palabra
                self.letras_usadas.append(guess)
                self.p1.vidas -= 1  # Quitar una vida
                if self.p1.vidas == 0:  # Si perdió todas las vidas:
                    self.game_over()
                    return  # Retornar de la función

    # Termina el juego cuando se gana o se pierde
    def game_over(self):
        self.is_game_over = True  # Terminar el juego
        self.display()

    # Actualiza lo mostrado en el terminal
    def display(self):
        cls()
        """
        1. Muestra las vidas disponibles. "\u2764\ufe0f")
        """
        # corazon = "<3"  # "\u2764\ufe0f"
        print("\t\t\tEL AHORCADO\n")
        print(f"Vidas: {self.p1.vidas}\t\t\t Letras erradas:  {self.letras_usadas}\n")
        print(f"Palabra: {self.mostrar_palabra}\n")
        if self.is_game_over:
            print(f"GAME OVER: {self.p1.vidas} lifes left\n\n")  # Mostrar en pantalla


palabra = "camarero"
game = Ahorcado(palabra)
game.play()