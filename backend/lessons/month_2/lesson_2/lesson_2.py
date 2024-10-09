



# class Transport:
#
#     def __init__(self, title, model, engine,):
#         self.title = title
#         self.model = model
#         self.engine = engine
#
#     def start_engine(self):
#         print(f'{self.title} {self.model} start engine!')
#
#
# class Car(Transport):
#
#     def __init__(self, title, model, engine, hp, nm):
#         super().__init__(title,model,engine)
#         self.hp = hp
#         self.nm = nm
#
#
#
# bmw = Car('bmw', '1999', 'v10',507,530)
# bmw.start_engine()


#
# class Car:
#
#     def start_engine(self):
#         print('its car start engine!')
#
# class Airplane:
#
#     def start_engine(self):
#         print(' its Airplane engine started ! and ready to fly!')


class Car:

    _current_speed = 0

    def __init__(self, title, model, max_speed, speed):
        self.title = title
        self.model = model
        self.max_speed = max_speed
        self.speed = speed

    def get_current_speed(self):
        print(self._current_speed)

    def gas(self):
        if self._current_speed >= self.max_speed:
            print('Check')
        else:
            self._current_speed += self.speed
            self.get_current_speed()

    def br(self):
        if self._current_speed - self.speed > 0:
            self._current_speed -= self.speed
            self.get_current_speed()


tiko = Car('tiko', 't',150, 10)


tiko.gas()
tiko.gas()
tiko.gas()

tiko.br()
tiko.br()
tiko.br()