class Vehicle:
    pass


class Sedan(Vehicle):
    def __init__(self, owner, model,color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = None
        self.set_color(color)

    def __repr__(self):
        print(f'Владелиц: {self.owner}\nМодель: {self.__model}\nМощность двигател(л/с): {self.__engine_power}'
              f'\nЦвет: {self.__color}')
    def get_color(self):
        return self.__color
    def set_color(self, color):
        __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
        if str(color).lower() in __COLOR_VARIANTS:
            self.__color = color
        else:
            print(f'Нельзя сменить цвет на {color}')



# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.__repr__()
print()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.__repr__()
