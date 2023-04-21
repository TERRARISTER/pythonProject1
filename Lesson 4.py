class Hello:
    def __init__(self):
        print("Hello!")
class Hello_World(Hello):
    def __init__(self):
        super().__init__()
        print("World!")
hello_world = Hello_World()

class Class1:
    var = 20
    def __init__(self):
        self.var = 10
class Class2(Class1):
    def __init__(self):
        print(self.var)
        super().__init__()
        print(self.var)
        print(super().var)
hello_world = Class2()

class Magnet:
    def __init__(self, strong, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.strong = strong
class Vacuum_Cleaner:
    def __init__(self, speed, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed = speed
class Window_Cleaner(Magnet, Vacuum_Cleaner ):
    def print_info(self):
        print(self.strong)
        print(self.speed)
Xiomi = Window_Cleaner()
Xiomi.print_info()

