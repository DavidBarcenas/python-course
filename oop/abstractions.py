class WashingMachine:
    def __init__(self) -> None:
        pass


    def wash(self, temperature = 'hot'):
        self._fill_water_tank(temperature)
        self._add_soap()
        self._wash()
        self._centrifuge()


    def _fill_water_tank(self, temperature):
        print(f'fill water tank {temperature}')


    def _add_soap(self):
        print('adding soap...')


    def _wash(self):
        print('washing up...')


    def _centrifuge(self):
        print('centrifuge...')


if __name__ == '__main__':
    washing_machine = WashingMachine()
    washing_machine.wash()