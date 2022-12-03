import time

class Juego:
    # Se inicializa el juego
    def __init__(self):
        self.inicializar_juego()
    # Se imprime el tablero
    def inicializar_juego(self):
        self.current_state = [['.','.','.'],
                              ['.','.','.'],
                              ['.','.','.']] 
        self.player_turn = 'X' 
    # Se imprime el tablero actual 
    def tablero(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()
    # Se comprueba que el movimiento insertado sea valido 
    def es_valido(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '.':
            return False
        else:
            return True
    # Se revisan las posibles formas de ganar
    def final(self):                                               
        for i in range(0, 3):
            if (self.current_state[0][i] != '.' and
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]
        # Victoria Vertical
        for i in range(0, 3):
            if (self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                return 'O'
        # Victorial en Diagonal 1
        if (self.current_state[0][0] != '.' and
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]
        # Victorial en Diagonal 2
        if (self.current_state[0][2] != '.' and
            self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]
        # Comprobamos que la tabla no este llena 
        for i in range(0, 3):
            for j in range(0, 3):
                if (self.current_state[i][j] == '.'):  # Si hay un espacio el juego continua 
                    return None
        # Empate
        return '.'
    # La IA es max
    def max_alpha_beta(self, alpha, beta):
            maxv = -2
            px = None
            py = None

            result = self.final()

            if result == 'X':
                return (-1, 0, 0)
            elif result == 'O':
                return (1, 0, 0)
            elif result == '.':
                return (0, 0, 0)

            for i in range(0, 3):
                for j in range(0, 3):
                    if self.current_state[i][j] == '.':
                        self.current_state[i][j] = 'O'
                        (m, min_i, in_j) = self.min_alpha_beta(alpha, beta)
                        if m > maxv:
                            maxv = m
                            px = i
                            py = j
                        self.current_state[i][j] = '.'

                        if maxv >= beta:
                            return (maxv, px, py)

                        if maxv > alpha:
                            alpha = maxv
            return (maxv, px, py)
    # El jugador humano es min
    def min_alpha_beta(self, alpha, beta):

            minv = 2
            qx = None
            qy = None

            result = self.final()

            if result == 'X':
                return (-1, 0, 0)
            elif result == 'O':
                return (1, 0, 0)
            elif result == '.':
                return (0, 0, 0)

            for i in range(0, 3):
                for j in range(0, 3):
                    if self.current_state[i][j] == '.':
                        self.current_state[i][j] = 'X'
                        (m, max_i, max_j) = self.max_alpha_beta(alpha, beta)
                        if m < minv:
                            minv = m
                            qx = i
                            qy = j
                        self.current_state[i][j] = '.'

                        if minv <= alpha:
                            return (minv, qx, qy)

                        if minv < beta:
                            beta = minv

            return (minv, qx, qy)
    #
    def play_alpha_beta(self):
        while True:
            self.tablero()
            self.result = self.final()

            if self.result != None:
                if self.result == 'X':
                    print('El Ganador es X!')
                elif self.result == 'O':
                    print('El Ganador es O!')
                elif self.result == '.':
                    print("Es un empate!")

                self.inicializar_juego()
                return

            if self.player_turn == 'X':
                while True:
                    (m, qx, qy) = self.min_alpha_beta(-2, 2)
                    print('Movimiento recomendado: X = {}, Y = {}'.format(qx, qy))
                    px = int(input('Insertar coordenadas de X: '))
                    py = int(input('Insertar coordenadas de Y: '))

                    qx = px
                    qy = py

                    if self.es_valido(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('EL movimiento es invalido! Intenta de nuevo.')

            else:
                (m, px, py) = self.max_alpha_beta(-2, 2)
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'

def main():
    g = Juego()
    g.play_alpha_beta()

if __name__ == "__main__":
    main()