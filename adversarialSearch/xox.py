from copy import deepcopy

class XOXGame:

    def __init__(self):
        self.state = {
            'board' : [['_' for j in range(3)] for i in range(3)],
            'player' : 'X'
        }

    def get_actions(self, state):
        return [(i,j, state['player']) for i in range(3) for j in range(3) if state['board'][i][j] == '_']

    def get_successor(self, state, action):
        i, j, p = action
        new_state = deepcopy(state)
        new_state['board'][i][j] = p
        new_state['player'] = 'X' if p == 'O' else 'O'
        return new_state

    def has_won(self, state, player):
        for i in range(3):
            if all(state['board'][i][j] == player for j in range(3)):
                return True
            if all(state['board'][j][i] == player for j in range(3)):
                return True

        if all(state['board'][i][i] == player for i in range(3)):
            return True
        if all(state['board'][i][2-i] == player for i in range(3)):
            return True

        return False

    def game_over(self, state):
        if self.has_won(state, 'X') or self.has_won(state, 'O'):
            return True
        return not any(state['board'][i][j] == '_' for i in range(3) for j in range(3))

    def get_utility(self, state):
        if self.has_won(state, 'X'):
            return float('inf')
        if self.has_won(state, 'O'):
            return float('-inf')
        x_open = 8
        o_open = 8

        for i in range(3):
            if any(state['board'][i][j] == 'X' for j in range(3)):
                o_open -= 1
            if any(state['board'][j][i] == 'X' for j in range(3)):
                o_open -= 1
            if any(state['board'][i][j] == 'O' for j in range(3)):
                x_open -= 1
            if any(state['board'][j][i] == 'O' for j in range(3)):
                x_open -= 1
            if any(state['board'][i][i] == 'X' for j in range(3)):
                o_open -= 1
            if any(state['board'][i][2-i] == 'X' for j in range(3)):
                o_open -= 1
            if any(state['board'][i][i] == 'O' for j in range(3)):
                x_open -= 1
            if any(state['board'][i][2-i] == 'O' for j in range(3)):
                x_open -= 1

        return x_open - o_open