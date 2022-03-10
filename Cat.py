class Cat:
    
    def __init__(self, age) -> None:
        self.age = age
    
    def mew(self):
        if self.age < 1:
            return self.getCuteMew()
        return self.getNormalMew()

    def getCuteMew(self):
        return "cute meeeeew"

    def getNormalMew(self):
        return "mew"

    def rideLicorne(self, licorne):
        return "I'm riding this %s", licorne
