# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
  def __init__(self, name, room):
    self.name = name
    self.room = room

    # inventory is a list that holds the Item's that are currently in the player's inventory
    self.inventory = []
  
  def listInventory(self):
    i = 1
    for e in self.inventory:
      print(f"{i} - {e}")
      i = i + 1