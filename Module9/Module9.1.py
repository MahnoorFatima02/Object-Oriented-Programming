# Question 1: car class with registration number, maximum speed, current speed and travelled distance.

class Car:

    def __init__(self, reg_number: str, max_speed: int):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0


if __name__ == "__main__":
    car_1 = Car("ABC-123", 142)
    print(vars(car_1))
