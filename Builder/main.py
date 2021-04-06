from abc import ABC


class Enemy(ABC):

    def __init__(self):
        self.hp = None
        self.image = None
        self.weapon = None

    def __str__(self):
        return f'{self.hp} | {self.image} | {self.weapon}'


class AbstractBuilder(ABC):

    def __init__(self):
        self.enemy = None

    def create_enemy(self):
        self.enemy = Enemy()


class Weapon():
    def __repr__(self):
        return self.__class__.__name__


class Gun(Weapon):
    pass


class MachineGun(Weapon):
    pass


class LightEnemy(AbstractBuilder):

    def add_hp(self):
        self.enemy.hp = 10

    def add_skin(self):
        self.enemy.image = 'image1'

    def add_weapon(self):
        self.enemy.weapon = Gun()


class HeavyEnemy(AbstractBuilder):

    def add_hp(self):
        self.enemy.hp = 20

    def add_skin(self):
        self.enemy.image = 'image2'

    def add_weapon(self):
        self.enemy.weapon = MachineGun()


class Director():

    def __init__(self, builder):
        self._builder = builder

    def construct_enemy(self):
        self._builder.create_enemy()
        self._builder.add_hp()
        self._builder.add_skin()
        self._builder.add_weapon()

    def get_enemy(self):
        return self._builder.enemy


concrete_builder = LightEnemy()
director = Director(concrete_builder)

director.construct_enemy()
enemy1 = director.get_enemy()
print(enemy1)

concrete_builder = HeavyEnemy()
director = Director(concrete_builder)
director.construct_enemy()
enemy2 = director.get_enemy()
print(enemy2)
