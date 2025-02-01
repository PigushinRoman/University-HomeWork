class Transport:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
       return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"
    

class Autobus(Transport): # Преподаватель на видео не обьяснял ни принципы ООП(ну то есть наследование, полиморфизм и т.д) ни переопределение методов в дочернем классе, ну да ладно.
    def seating_capacity(self, capacity = 50):
         return super().seating_capacity(capacity)


print(Autobus('Renaul Logan',120,50).seating_capacity())