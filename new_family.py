def start():
    class Parent:
        """Данный класс создает объект 'Родитель'"""
        def __init__(self, name: str, age: int, children: list):
            self.name = name
            self.age = age
            self.children = children

        def print_info(self):
            """Данный метод возвращает основную информацию о родителе"""
            print(f'Меня зовут {self.name}, мне {self.age} лет и у меня {len(self.children)} детей')

        def child_conditions_all(self):
            """Метод позволяет вывести информацию о состоянии детей родителя"""
            for child in self.children:
                child.print_info_state_hunger()
                child.print_info_state_calm()

        def calm_down_child(self):
            """Метод позволяет успокоить ребенка"""
            for child in self.children:
                child.calm_down()

        def feed_child(self):
            """Метод позволяет покормить ребенка"""
            for child in self.children:
                child.eats()

    class Child:
        """Данный класс создает объект 'Ребенок'"""
        HUNGER_LEVELS = {0: 'голоден', 1: 'не голоден'}
        CALM_LEVELS = {0: 'раздражен', 1: 'слегка капризничает', 2: 'спокоен'}

        def __init__(self, name_child, age_child, state_hunger=0, state_calm=0):
            self.name_child = name_child
            self.age_child = age_child
            self.state_hunger = state_hunger
            self.state_calm = state_calm

        def eats(self):
            """Метод позволяет изменить состояние голода ребенка"""
            if not self.state_hunger:
                self.state_hunger += 1
                print(f'{self.name_child} покормлен')
            else:
                self.print_info_state_hunger()

        def calm_down(self):
            """Метод позволяет изменить состояние спокойствия ребенка"""
            if self.state_calm < 2:
                self.state_calm += 1
                print(f'Успокаиваем {self.name_child}')
                if self.state_calm < 2:
                    print(f'{self.name_child} немного успокоился, но еще все равно не в лучшем настроении!')
                else:
                    self.print_info_state_calm()
            else:
                self.print_info_state_calm()

        def print_info_state_hunger(self):
            """Метод выводит информацию о состоянии голода ребенка"""
            print(f'{self.name_child} сейчас {self.HUNGER_LEVELS[self.state_hunger]}')

        def print_info_state_calm(self):
            """Метод выводит информацию о состоянии спокойствия ребенка"""
            print(f'{self.name_child} сейчас {self.CALM_LEVELS[self.state_calm]}')

    name_parrent, age_parrent = 'Anton', 35
    name_child, age_child, state_hunger, state_calm = ['Darina', 'Sava'], [18, 3], [1, 0], [1, 0]
    count_child = 2
    children = []
    for index in range(count_child):
        if age_child[index] >= age_parrent - 16:
            print('Ребенок должен быть младше родителя на 16 лет!')
        else:
            children.append(Child(name_child[index], age_child[index], state_hunger[index], state_calm[index]))
    parent = Parent(name_parrent, age_parrent, children)
    return parent


if __name__ == '__main__':
    start()
