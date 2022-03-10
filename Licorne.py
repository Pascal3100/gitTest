class Licorne:

    THE_MAXIMUM = 100

    def __init__(self, fabulousness) -> None:
        self.fabulousness = fabulousness

    def run(self):
        if self.fabulousness > self.THE_MAXIMUM:
            return self.sparklesEverywhere()
        else:
            return "I'm juste a horse buddy"

    def sparklesEverywhere(self):
        return "SPARKLES!!!! AND MORE!"