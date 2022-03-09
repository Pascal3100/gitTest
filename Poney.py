from mimetypes import init
from pdb import runeval


class Poney:
    def __init__(self, runLevel) -> None:
        self.runLevel = runLevel

    def run(self):
        if self.runLevel > 3:
            return "Pataclop Pataclop!"
        return "Trot Trot Trot..."