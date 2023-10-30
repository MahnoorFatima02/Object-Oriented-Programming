# Question 2: Accelerate Method

class Car:

    def __init__(self, reg_number: str, max_speed: int):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

    def accelerate(self, change_speed: int):
        if self.max_speed < self.current_speed + change_speed:
            self.current_speed = self.max_speed
        elif self.current_speed + change_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = self.current_speed + change_speed

    def get_current_speed(self):
        return self.current_speed


if __name__ == "__main__":
    car_1 = Car("ABC-123", 240)
    car_1.accelerate(+30)
    car_1.accelerate(+50)
    car_1.accelerate(+70)
    print(car_1.get_current_speed())
    car_1.accelerate(-200)
    print(car_1.get_current_speed())
