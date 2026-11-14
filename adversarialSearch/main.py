from xox import XOXGame
from agent import RandomAgent, MiniMaxAgent, AlphaBetaAgent

game = XOXGame()
agent = AlphaBetaAgent(game, 9) #MiniMaxAgent(game, 1)  #RandomAgent(game)
agent.game_loop()