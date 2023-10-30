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


if __name__ == "__main__":

    max_distance = 10000
    max_distance_covered = 0
    winning_car = ""
    car_list = []

    for i in range(1, 11):
        car_list.append(Car("ABC-" + str(i), random.randint(100, 200)))

    hr = 0
    while max_distance_covered < max_distance:

        current_distance_of_car = 0
        for car in car_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
            if current_distance_of_car < car.get_distance():
                current_distance_of_car = car.get_distance()
                winning_car = car.get_reg_number()

        hr = hr + 1

        max_distance_covered = current_distance_of_car

    print(f"The winner of race is : {winning_car}")

    t = PrettyTable(['Reg_no', 'maximum_speed', 'current_speed', 'maximum_distance'])
    for car in car_list:
        t.add_row([car.get_reg_number(), car.get_max_speed(), car.get_current_speed(), car.get_distance()])
    print(t)
