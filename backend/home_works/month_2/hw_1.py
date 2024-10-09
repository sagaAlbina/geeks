

class SuperHero:
    people = 'people'

    def __init__(self, name, nickname,superpower,
                 health_points, catchphrase ):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def HeroName(self):
        print(f'Hero name: {self.name}')

    def HealthPoints(self):
        print(f'{self.health_points}' * 2 , 'health')
    def __str__(self):
        return (f'nickname of the hero: {self.nickname}  '
                f'Supepower: {self.superpower}  '
                f'Hero health: {self.health_points}')
    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero('Fiola', 'Fi', 'super fast',
                 'best', 'i just started!')


hero.HeroName()
hero.HealthPoints()
phrases = hero.catchphrase
print(hero)
print("lenght of the hero's catchphrase: ", len(phrases))
















