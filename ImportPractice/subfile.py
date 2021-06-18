class A:
    def __init__(self):
        self.first = 1
        self.last = 22
        self.phrase = "works great!"

    def calc(self):
        print(self.first + self.last, "= 23. ", self.phrase)

class B(A):
    def __init__(self, phrase):
        super().__init__()
        self.phrase = phrase
    
    def changePhrase(self, newPhrase):
        print(f"The old phrase was {self.phrase}, but the new phrase is {newPhrase}.")
        self.phrase = newPhrase