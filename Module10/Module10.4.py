import random
from prettytable import PrettyTable


# Question 4: Race Program
class Car:

    def __init__(self, reg_number: str, max_speed: int):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

    def accelerate(self, speed: int):
        if self.max_speed < self.current_speed + speed:
            self.current_speed = self.max_speed
        elif self.current_speed + speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = self.current_speed + speed

    def get_reg_number(self):
        return self.reg_number

    def get_current_speed(self):
        return self.current_speed

    def get_distance(self):
        return self.distance

    def get_max_speed(self):
        return self.max_speed

    def drive(self, hour):
        dist_covered = self.current_speed * hour
        self.distance = self.distance + dist_covered


class Race:
    def __init__(self, name: str, distance: int, car_list: list):
        self.name = name
        self.distance = distance
        self.car_list = car_list
        self.reached_finish_line = False

    def hour_passes(self):
        for car in car_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        t = PrettyTable(['Reg_no', 'maximum_speed', 'current_speed', 'maximum_distance'])
        for car in car_list:
            t.add_row([car.get_reg_number(), car.get_max_speed(), car.get_current_speed(), car.get_distance()])
        print(t)

    def race_finished(self):
        for car in car_list:
            if car.distance >= self.distance:
                self.reached_finish_line = True
                break

        return self.reached_finish_line


if __name__ == "__main__":

    car_list = []
    for i in range(1, 11):
        car_list.append(Car("ABC-" + str(i), random.randint(100, 200)))

    race_1 = Race("Grand_Demolition_Derby", 8000, car_list)

    hr = 0
    while not race_1.race_finished():
        race_1.hour_passes()
        hr = hr + 1

        if hr % 10 == 0:
            race_1.print_status()

    race_1.print_status()
