class Fish:
    def __init__(self, sex, species) -> None:
        self.sex = sex
        self.species = species

    def description(self):
        return f'This {self.species} is {self.sex}'


class Skalar(Fish):
    def __init__(self, height, colour):
        self.height = height
        self.colour = colour


Skalar = Fish('male', 'Skalar')
print(Skalar.description())
Skalar.colour = 'red'
print(Skalar.colour, Skalar.species)

Joseph = Fish('male', Skalar)
print(Joseph.description())
Joseph.colour = 'red'
print(Joseph.colour)

Bronek = Fish('male', 'Skalar')
print(Bronek.description())
Bronek.height = 15
print(Bronek.height)

Janosik = Fish('male', 'Mieczyk')
Janosik.height = 15
print(Janosik.height)
