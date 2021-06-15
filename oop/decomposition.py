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
        