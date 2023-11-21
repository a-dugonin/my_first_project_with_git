def start():

    HUNGER_LEVELS = {0: 'голоден', 1: 'не голоден'}
    CALM_LEVELS = {0: 'раздражен', 1: 'слегка капризничает', 2: 'спокоен'}

    class Parent:
        """Данный класс создает объект 'Родитель'"""
        def __init__(self, name: str, age: int, children: dict):
            """Конструктор класса Parent"""
            self.name = name
            self.age = age
            self.children = children

        def __str__(self):
            """Геттер, возвращает основную информацию о родителе"""
            return f'Меня зовут {self.name}, мне {self.age} лет и у меня {len(children)} детей'

        def child_conditions_all(self, name_child=''):
            """Метод позволяет вывести информацию о состоянии детей родителя"""
            if not name_child:
                for child in self.children:
                    print(f'{child} {HUNGER_LEVELS[children[child].state_hunger]} и {CALM_LEVELS[children[child].state_calm]}')
            else:
                print(f'{name_child} {HUNGER_LEVELS[children[name_child].state_hunger]} и {CALM_LEVELS[children[name_child].state_calm]}')

        def calm_down_child(self, name_child=''):
            """Метод позволяет успокоить ребенка при указании его имени или сразу всех детей"""
            if not name_child:
                for child in self.children:
                    if children[child].state_calm < 2:
                        self.children[child].change_state_calm()
                        print(f'Успокаиваем {child}. {child} сейчас {CALM_LEVELS[children[child].state_calm]}')
                    else:
                        print(f'{child} спокоен')
            else:
                if children[name_child].state_calm < 2:
                    self.children[name_child].change_state_calm()
                    print(f'Успокаиваем {name_child}. {name_child} сейчас {CALM_LEVELS[children[name_child].state_calm]}')
                else:
                    print(f'{name_child} спокоен')

        def feed_child(self, name_child=''):
            """Метод позволяет покормить ребенка при указании его имени или сразу всех детей"""
            if not name_child:
                for child in self.children:
                    if not children[child].state_hunger:
                        self.children[child].change_state_hunger()
                        print(f'{child} покормлен')
                    else:
                        print(f'{child} не голоден')
            else:
                if not children[name_child].state_hunger:
                    self.children[name_child].change_state_hunger()
                    print(f'{name_child} покормлен')
                else:
                    print(f'{name_child} не голоден')

    class Child:
        """Данный класс создает объект 'Ребенок'"""

        def __init__(self, name_child, age_child, state_hunger=0, state_calm=0):
            """Конструктор класса Child"""
            self.name_child = name_child
            self.age_child = age_child
            self.state_hunger = state_hunger
            self.state_calm = state_calm

        def change_state_hunger(self):
            """Метод позволяет изменить состояние голода ребенка"""
            self.state_hunger += 1

        def change_state_calm(self):
            """Метод позволяет изменить состояние спокойствия ребенка"""
            self.state_calm += 1

    name_parrent, age_parrent = 'Anton', 35
    name_child, age_child, state_hunger, state_calm = ['Darina', 'Sava'], [18, 3], [1, 0], [1, 0]
    count_child = 2
    children = {}
    for index in range(count_child):
        if age_child[index] >= age_parrent - 16:
            print('Ребенок должен быть младше родителя на 16 лет!')
        else:
            children[name_child[index]] = Child(name_child[index], age_child[index], state_hunger[index], state_calm[index])
    parent = Parent(name_parrent, age_parrent, children)
    return parent


if __name__ == '__main__':
    start()
