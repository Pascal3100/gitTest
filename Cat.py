class Cat:
    
    def __init__(self, age) -> None:
        self.age = age
    
    def mew(self):
        if self.age < 1:
            return "cute meeeeew"
        return "mew"
