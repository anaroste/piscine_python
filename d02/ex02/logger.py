import time
from random import randint
import os


def log(func):
    def funct_log(*args, **kwargs):
        userTab = os.path.expanduser('~').split('/')
        user = userTab[len(userTab) - 1]
        funct_name = func.__name__

        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        tmp_time = end - start
        if tmp_time > 1:
            funct_time = round(tmp_time, 3)
            nota = 's'
        else:
            funct_time = round(tmp_time * 1000, 3)
            nota = 'ms'
        s = '({})Running: {:20}[ exec-time = {} {} ]\n'.format(
            user, funct_name, funct_time, nota)
        with open("machine.log", 'a') as f:
            f.write(s)
        return ret
    return funct_log


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
