import random
import time

class Agent:

    def __init__(self, game):
        self.game = game

    def decision(self):
        pass

    def game_loop(self):
        while True:
            t0 = time.perf_counter()
            action = self.decision()
            t1 = time.perf_counter()
            print(f'{t1-t0}s')
            self.game.state = self.game.get_successor(self.game.state, action)
            print(*self.game.state['board'], sep= '\n')
            print()

            if self.game.game_over(self.game.state):
                print('Game over')
                break

            i = int(input())
            j = int(input())
            self.game.state = self.game.get_successor(self.game.state, (i, j, 'O'))
            print(*self.game.state['board'], sep= '\n')
            print()
            if self.game.game_over(self.game.state):
                print('Game Over')
                break


class RandomAgent(Agent):

    def decision(self):
        return random.choice(self.game.get_actions(self.game.state))

class MiniMaxAgent(Agent):

    def __init__(self, game, max_depth):
        super().__init__(game)
        self.max_depth = max_depth

    def decision(self):
        best_v = float('-inf')
        best_a = None

        for a in self.game.get_actions(self.game.state):
            v = self.min_value(self.game.get_successor(self.game.state, a), 1)
            if best_v < v:
                best_v = v
                best_a = a
        return best_a

    def max_value(self, state, d):
        # if self.game.has_won(state, 'X'):
        #     return float('inf')
        # if self.game.has_won(state, 'O'):
        #     return float('-inf')
        # if self.game.game_over(state):
        #     return 0

        if self.game.game_over(state) or d == self.max_depth:
            return self.game.get_utility(state)
        best_v = float('-inf')
        for a in self.game.get_actions(state):
            v = self.min_value(self.game.get_successor(state, a), d + 1)
            if best_v < v:
                best_v = v
        return best_v
        

    def min_value(self, state, d):
        # if self.game.has_won(state, 'X'):
        #     return float('inf')
        # if self.game.has_won(state, 'O'):
        #     return float('-inf')
        # if self.game.game_over(state):
        #     return 0

        if self.game.game_over(state) or d == self.max_depth:
            return self.game.get_utility(state)
        best_v = float('inf')
        for a in self.game.get_actions(state):
            v = self.max_value(self.game.get_successor(state, a), d + 1)
            if best_v > v:
                best_v = v
        return best_v


class AlphaBetaAgent(Agent):

    def __init__(self, game, max_depth):
        super().__init__(game)
        self.max_depth = max_depth

    def decision(self):
        alpha = float('-inf')
        beta = float('inf')
        best_v = float('-inf')
        best_a = None

        for a in self.game.get_actions(self.game.state):
            v = self.min_value(self.game.get_successor(self.game.state, a), 1, alpha, beta)
            alpha = max(alpha, v)
            if best_v < v:
                best_v = v
                best_a = a
        return best_a

    def max_value(self, state, d, alpha, beta):
        if self.game.game_over(state) or d == self.max_depth:
            return self.game.get_utility(state)
        best_v = float('-inf')
        for a in self.game.get_actions(state):
            v = self.min_value(self.game.get_successor(state, a), d + 1, alpha, beta)
            alpha = max(alpha, v)
            if best_v < v:
                best_v = v
            if alpha > beta:
                break
        return best_v
        

    def min_value(self, state, d, alpha, beta):
        if self.game.game_over(state) or d == self.max_depth:
            return self.game.get_utility(state)
        best_v = float('inf')
        for a in self.game.get_actions(state):
            v = self.max_value(self.game.get_successor(state, a), d + 1, alpha, beta)
            beta = min(beta, v)
            if best_v > v:
                best_v = v
            if alpha > beta:
                break
        return best_v

