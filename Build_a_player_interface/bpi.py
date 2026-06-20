from abc import ABC, abstractmethod
import random

class Player(ABC):
   """abstract class defining the player"""
   def __init__(self) -> None:
       self.moves = []
       self.position = (0, 0)
       self.path = [self.position]


   def make_move(self) -> tuple:
       move = random.choice(self.moves)
       #new_position = tuple(sum(x) for x in zip(self.position, move))
       #self.position = new_position
       new_position = (self.position[0] + move[0], self.position[1] + move[1])
       """new_x = self.position[0] + move[0]
       new_y = self.position[1] + move[1]
       self.position = (new_x, new_y)"""
       self.position = new_position
       self.path.append(self.position)
       return self.position
  
   @abstractmethod
   def level_up(self) -> None:
       pass
  
class Pawn(Player):
   def __init__(self):
       super().__init__()
       self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]


   def level_up(self):
       self.moves += [(1, 1), (1, -1), (-1, -1), (-1, 1)]
