class Person:
    def __init__(self, name) -> None:
        self.name = name

    
    def move(self):
        print('I am walking')


class Cyclist(Person):
    def __init__(self, name) -> None:
        super().__init__(name)


    def move(self):
        print('I am moving on my bike')


def run():
    person = Person('David')
    person.move()

    cyclist = Cyclist('Jhon')
    cyclist.move()


if __name__ == '__main__':
    run()