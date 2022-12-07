from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
   
  

    def __init__(self):
        """Constructs a new Artifact (object on the screen)."""
        super().__init__()
        self._points = 0

    def calculate_points(self,artifact):
        

        if artifact.get_text == "*":
            return 1
        else:
           return -1

       
    