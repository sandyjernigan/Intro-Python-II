# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description):
    # The room should have `name` and `description` attributes.
    self.name = name
    self.shortname = shortname
    self.description = description

    # The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
    # which point to the room in that respective direction.
    self.n_to = None
    self.e_to = None
    self.s_to = None
    self.w_to = None

    # storage is a list that holds the Item's that are currently in the room
    self.storage = []

  def __str__(self):
    return f"{self.shortname}"
  
  def listStorage(self):
    i = 1
    for e in self.storage:
      print(f"{i} - {e}")
      i = i + 1
  