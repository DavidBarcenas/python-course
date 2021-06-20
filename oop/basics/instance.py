class Car:
    def __init__(self, model, brand, color) -> None:
        self.model = model
        self.brand = brand
        self.color = color
        self._status = 'neutral'
        self._motor = Motor(cylinders = 4)

    
    def acelerate(self, speed_up = 'low'):
        if speed_up == 'fast':
            self._motor.inject_gasoline(10)
        else:
            self._motor.inject_gasoline(3)

        self._status = 'drift'


class Motor:
    def __init__(self, cylinders, motor_type = 'gasoline') -> None:
        self.cylinders = cylinders
        self.motor_type = motor_type
        self._temperature = 0

    
    def inject_gasoline(self, amount):
        pass


class Coordinate:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


    def distance(self, coord):
        x_diff = (self.x - coord.x)**2
        y_diff = (self.y - coord.y)**2

        return (x_diff + y_diff)**0.5
        

if __name__ == '__main__':
    coord_1 = Coordinate(3, 30)
    coord_2 = Coordinate(4, 8)

    # print(coord_1.distance(coord_2))
    print(isinstance(coord_2, Coordinate))