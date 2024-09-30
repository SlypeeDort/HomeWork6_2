class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = None
        self.set_color(color)
    def print_info(self):
        print(f'nМодель: {self.__model}\nМощность двигател(л/с): {self.__engine_power}'
              f'\nЦвет: {self.__color}\nВладелиц: {self.owner}')

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def set_color(self, color):
        if color.lower() in self.__COLOR_VARIANTS:
            print(f'Покрасили в: {color}')
            self.__color = color
        else:
            print(f'Нельзя сменить цвет на {color}')


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)
vehicle1.print_info()
print()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()

