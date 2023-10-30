# Question 3: Drive Method

class Car:

    def __init__(self, reg_number: str, max_speed: int):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 2000

    def accelerate(self, speed: int):
        if self.max_speed < self.current_speed + speed:
            self.current_speed = self.max_speed
        elif self.current_speed + speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = self.current_speed + speed

    def drive(self, hour):
        dist_covered = self.current_speed * hour
        self.distance = self.distance + dist_covered

    def get_distance(self):
        print(f"The distance covered by car is {self.distance} km")

if __name__ == "__main__":

    car_1 = Car("ABC-123", 240)
    car_1.get_distance()
    car_1.accelerate(+60)
    car_1.drive(1.5)
    car_1.get_distance()